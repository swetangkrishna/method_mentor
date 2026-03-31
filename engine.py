from __future__ import annotations

from typing import Iterable

from .methods import format_method_options, generate_method_options
from .parsers import (
    classify_fit,
    detect_method_name_if_present,
    extract_topic_if_possible,
    infer_evidence_orientation,
    infer_methods_confidence,
    infer_methods_experience_level,
    infer_programme_type,
    infer_research_purpose,
    infer_study_mode,
    infer_uncertainty_level,
    infer_year,
)
from .state import MethodReflection, SessionState
from .templates import (
    DIRECT_CHOICE_REDIRECT,
    REFLECTION_QUESTIONS,
    STAGE_1_PROMPT,
    STAGE_2_PROMPT,
    STAGE_3_QUESTIONS,
    STAGE_6_PROMPT,
    WELCOME_TEXT,
)


class MethodCheckEngine:
    def __init__(self) -> None:
        self.state = SessionState()

    def run_cli(self) -> None:
        print(WELCOME_TEXT)
        print()
        self._handle_stage_1()
        self._handle_stage_2()
        self._handle_stage_3()
        self._handle_stage_4()
        self._handle_stage_5()
        self._handle_stage_6()
        self.state.status = "completed"
        print("\nSession complete. Thank you for using MethodCheck.")

    def _ask(self, prompt: str, question_key: str | None = None) -> str:
        self.state.log("assistant", self.state.current_stage, prompt, question_key)
        print(prompt)
        answer = input("> ").strip()
        self.state.log("user", self.state.current_stage, answer, question_key)
        return answer

    def _ack(self, text: str) -> None:
        self.state.log("assistant", self.state.current_stage, text, "ack")
        print(text)

    def _handle_stage_1(self) -> None:
        answer = self._ask(STAGE_1_PROMPT, "initial_prompt")
        self.state.research_question_raw = answer
        self.state.research_topic = extract_topic_if_possible(answer)
        self.state.proposed_method_initial = detect_method_name_if_present(answer)
        self.state.uncertainty_level = infer_uncertainty_level(answer)
        self._ack("That sounds like a thoughtful starting point. It is very normal to still be weighing up methods at this stage.")
        self.state.transition("stage_2_onboarding")

    def _handle_stage_2(self) -> None:
        answer = self._ask(STAGE_2_PROMPT, "onboarding")
        self.state.programme_type = infer_programme_type(answer)
        self.state.study_mode = infer_study_mode(answer)
        self.state.year_of_study = infer_year(answer)
        self.state.methods_confidence_preference = infer_methods_confidence(answer)
        self.state.methods_experience_level = infer_methods_experience_level(answer)
        self._ack("That is helpful context. Your prior comfort with one type of method can be useful to know, but it does not necessarily mean that is the only good fit for your question.")
        self.state.transition("stage_3_clarification")

    def _handle_stage_3(self) -> None:
        for key, prompt in STAGE_3_QUESTIONS:
            answer = self._ask(prompt, key)
            if key == "research_purpose":
                self.state.research_purpose = infer_research_purpose(answer)
            elif key == "data_type_preference":
                self.state.data_type_preference = answer
            elif key == "evidence_orientation":
                self.state.evidence_orientation = infer_evidence_orientation(answer)
            elif key == "context_clarification":
                self.state.research_context_notes = answer
            self._ack("That is a useful consideration.")
        self.state.transition("stage_4_methods")

    def _handle_stage_4(self) -> None:
        self.state.generated_methods = generate_method_options(self.state)
        self.state.reflection_order = [m.method_id for m in self.state.generated_methods]
        for method in self.state.generated_methods:
            self.state.reflections_by_method[method.method_id] = MethodReflection(method_id=method.method_id)
        output = format_method_options(self.state.generated_methods)
        self.state.log("assistant", self.state.current_stage, output, "methods_presented")
        print(output)
        self.state.transition("stage_5_reflection")

    def _handle_stage_5(self) -> None:
        for method in self.state.generated_methods:
            print()
            intro = f"Let's take **{method.method_name}** first and think about whether it would work well in practice for your project."
            self.state.log("assistant", self.state.current_stage, intro, "method_intro")
            print(intro)
            reflection = self.state.reflections_by_method[method.method_id]
            for key, prompt in REFLECTION_QUESTIONS:
                answer = self._ask(prompt, key)
                setattr(reflection, key, classify_fit(answer))
                reflection.raw_notes[key] = answer
                self._ack("That makes sense.")
            summary = self._summarize_method_reflection(method.method_name, reflection)
            self.state.log("assistant", self.state.current_stage, summary, "method_summary")
            print(summary)
        self.state.transition("stage_6_summary")

    def _handle_stage_6(self) -> None:
        answer = self._ask(STAGE_6_PROMPT, "final_summary")
        if self._is_direct_choice_request(answer):
            print(DIRECT_CHOICE_REDIRECT)
        self.state.student_tentative_choice = answer
        self.state.student_reasoning_summary = answer
        self.state.supervisor_discussion_points = "Bring the current rationale, remaining uncertainties, and any access or analysis questions to the supervisor."
        closing = (
            "It sounds like you now have a clearer sense of which method may fit your question and context. "
            "That does not mean everything has to be fully settled yet, but you have a stronger basis for discussing it with your supervisor."
        )
        self.state.log("assistant", self.state.current_stage, closing, "closing")
        print(closing)

    def _summarize_method_reflection(self, method_name: str, reflection: MethodReflection) -> str:
        strengths = self._count_matches(
            [
                reflection.timeline_fit,
                reflection.participant_access_fit,
                reflection.analysis_skills_fit,
                reflection.ethics_consideration,
                reflection.research_question_alignment,
                reflection.depth_breadth_fit,
            ],
            {"good_fit"},
        )
        constraints = self._count_matches(
            [
                reflection.timeline_fit,
                reflection.participant_access_fit,
                reflection.analysis_skills_fit,
                reflection.ethics_consideration,
                reflection.research_question_alignment,
                reflection.depth_breadth_fit,
            ],
            {"poor_fit", "possible_with_constraints"},
        )
        return (
            f"So far, it sounds like {method_name} could offer some useful value for your question, "
            f"with around {strengths} area(s) currently feeling like a good fit and {constraints} area(s) needing closer thought."
        )

    @staticmethod
    def _count_matches(values: Iterable[str], targets: set[str]) -> int:
        return sum(1 for value in values if value in targets)

    @staticmethod
    def _is_direct_choice_request(text: str) -> bool:
        lowered = text.lower()
        return any(phrase in lowered for phrase in ["just tell me", "best method", "choose for me", "which one should i use"])
