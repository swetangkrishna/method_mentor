from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional
import uuid


STAGES = (
    "stage_1_initial",
    "stage_2_onboarding",
    "stage_3_clarification",
    "stage_4_methods",
    "stage_5_reflection",
    "stage_6_summary",
)


@dataclass
class Message:
    role: str
    stage: str
    content: str
    question_key: Optional[str] = None
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


@dataclass
class MethodOption:
    method_id: str
    method_name: str
    method_type: str
    description_plain: str
    relevance_reason: str
    example_context: str
    comfort_zone_relation: str


@dataclass
class MethodReflection:
    method_id: str
    timeline_fit: str = "not_yet_discussed"
    participant_access_fit: str = "not_yet_discussed"
    analysis_skills_fit: str = "not_yet_discussed"
    ethics_consideration: str = "not_yet_discussed"
    research_question_alignment: str = "not_yet_discussed"
    depth_breadth_fit: str = "not_yet_discussed"
    raw_notes: Dict[str, str] = field(default_factory=dict)


@dataclass
class SessionState:
    session_id: str = field(default_factory=lambda: f"sess_{uuid.uuid4().hex[:8]}")
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    status: str = "active"
    current_stage: str = "stage_1_initial"
    completed_stages: List[str] = field(default_factory=list)
    message_history: List[Message] = field(default_factory=list)

    programme_type: Optional[str] = None
    study_mode: Optional[str] = None
    year_of_study: Optional[str] = None
    methods_confidence_preference: Optional[str] = None
    methods_experience_level: Optional[str] = None

    research_question_raw: Optional[str] = None
    research_topic: Optional[str] = None
    proposed_method_initial: Optional[str] = None
    uncertainty_level: Optional[str] = None
    research_purpose: Optional[str] = None
    data_type_preference: Optional[str] = None
    evidence_orientation: Optional[str] = None
    research_context_notes: Optional[str] = None

    generated_methods: List[MethodOption] = field(default_factory=list)
    reflection_order: List[str] = field(default_factory=list)
    reflections_by_method: Dict[str, MethodReflection] = field(default_factory=dict)

    student_tentative_choice: Optional[str] = None
    student_reasoning_summary: Optional[str] = None
    remaining_uncertainties: Optional[str] = None
    supervisor_discussion_points: Optional[str] = None

    def log(self, role: str, stage: str, content: str, question_key: Optional[str] = None) -> None:
        self.message_history.append(Message(role=role, stage=stage, content=content, question_key=question_key))
        self.updated_at = datetime.utcnow().isoformat()

    def transition(self, next_stage: str) -> None:
        if self.current_stage not in self.completed_stages:
            self.completed_stages.append(self.current_stage)
        self.current_stage = next_stage
        self.updated_at = datetime.utcnow().isoformat()
