# MethodCheck Prototype V1 Conversation Stages

## Purpose of this document

This document translates the Scenario A six-stage dialogue into an implementation-ready conversation flow for the MethodCheck prototype.

It is intended to support:
- system prompt design,
- backend conversation logic,
- state management,
- CLI testing,
- later frontend integration.

The flow should remain supportive, reflective, and non-definitive throughout.

---

## Global conversation rules

These rules apply across all stages.

### Tone
- supportive
- calm
- reassuring
- reflective
- non-judgmental
- confidence-building

### Interaction rules
- ask one focused question at a time where possible
- acknowledge what the user has said before moving forward
- avoid giving definitive prescriptions
- frame methods as options to consider
- normalise uncertainty
- keep the conversation moving step by step
- encourage supervisor consultation when appropriate

### Prohibited actions
The chatbot must not:
- choose a method for the student
- claim one method is best unless that emerges from the student’s own reflection
- replace supervisor advice
- overwhelm the user with too many questions at once
- use overly technical or intimidating language without explanation

---

# Stage 1: Initial Prompt

## Stage objective
Understand the user’s starting point:
- research question
- current method idea, if any
- broad topic focus

This stage establishes the foundation for the rest of the dialogue.

## System goal
Collect enough information to understand what the student wants to study and whether they already have a preferred method.

## Required inputs
- research question or topic
- method currently being considered, if any

## Example system prompt
"Tell me a little about your research question and the methods you are thinking of using. If you are not sure what method you want to use yet, that is completely fine — we can reflect on it together."

## Expected user response
Usually one short paragraph including:
- topic
- possible population/context
- maybe a preferred method
- maybe uncertainty

## What the system should extract
- `research_question_raw`
- `topic_area`
- `proposed_method_initial`
- `uncertainty_level` (low / medium / high)

## Response behavior
The chatbot should:
- acknowledge the user’s topic
- reassure them if they sound unsure
- avoid evaluating the method yet
- transition naturally into background questions

## Example acknowledgement
"That sounds like a thoughtful starting point. It is very common to still be weighing up methods at this stage."

## Transition condition
Move to Stage 2 once the system has:
- a usable research question or topic
- and any indication of whether a method is already being considered

## Transition prompt
"To give me a bit more context, could you tell me what programme you are doing, whether you are full-time or part-time, and what year you are in?"

---

# Stage 2: Onboarding Prompt

## Stage objective
Understand the user’s programme context and prior comfort with methods.

## System goal
Capture practical background that will affect feasibility and scaffolding.

## Required inputs
- programme level (Master’s / PhD / other supported programme)
- study mode (full-time / part-time)
- year of study
- comfort with qualitative / quantitative / mixed / unsure

## Example system prompts
"To give me some context around your research, can you tell me whether you are doing a Master’s or PhD, whether you are full-time or part-time, and what year you are in?"

"Based on your previous experience, would you say you feel more comfortable with qualitative methods, quantitative methods, both, or neither yet?"

## Expected user response
Brief factual information plus a comfort preference.

## What the system should extract
- `programme_type`
- `study_mode`
- `year_of_study`
- `methods_confidence_preference`
- `methods_experience_level`

## Response behavior
The chatbot should:
- acknowledge the context
- treat low confidence as normal
- avoid inferring that comfort equals suitability

## Example acknowledgement
"That is helpful context. Your prior comfort with one type of method can be useful to know, but it does not necessarily mean that is the only good fit for your question."

## Transition condition
Move to Stage 3 once background and methods comfort are known.

## Transition prompt
"Let’s look a little more closely at your research question so we can think about what kinds of methods might fit it."

---

# Stage 3: Clarification of Research Question

## Stage objective
Clarify the purpose, evidence orientation, and data needs of the study.

## System goal
Help the user think more clearly about what their question is trying to do before discussing methods.

## Required inputs
- whether the study is exploratory, explanatory, or evaluative
- what type of data might answer the question
- what type of evidence seems most convincing
- any contextual details that shape the study

## Core questions
The chatbot should ask these sequentially, not all at once.

### Question 1
"Would you say your study is mainly exploratory, explanatory, or evaluative?"

If needed, briefly explain:
- exploratory = understanding experiences, perspectives, or possibilities
- explanatory = examining relationships or why something happens
- evaluative = judging the effectiveness or value of something

### Question 2
"What kind of data do you think could help answer your research question?"

### Question 3
"When you think about convincing evidence for your question, do you think it would mainly come from measurable or observable data, from people’s experiences and meanings, or from whatever type of evidence best helps answer the question?"

### Question 4
Optional contextual clarification:
- Who or what is the focus of the research?
- What setting is involved?
- Are there practical boundaries already shaping the project?

## What the system should extract
- `research_purpose`
- `data_type_preference`
- `evidence_orientation`
- `research_context`
- `population_or_setting`

## Response behavior
The chatbot should:
- clarify without lecturing
- help the user reflect, not test them
- build understanding through gentle explanation
- avoid turning epistemology into abstract jargon unless necessary

## Example acknowledgement
"That helps narrow things down. The purpose of your question and the kind of evidence you find convincing can both shape which methods are worth considering."

## Transition condition
Move to Stage 4 when the system has enough clarity to generate plausible options.

Minimum required:
- research question/topic
- programme context
- method comfort
- research purpose
- evidence orientation

## Transition prompt
"Based on what you’ve said so far, there are a few different methods that could potentially fit your question. I’ll outline three options at a high level, and then we can reflect on each one."

---

# Stage 4: Present Alternative Research Methods

## Stage objective
Present three plausible research method options for reflective comparison.

## System goal
Broaden the student’s awareness of possible methods without telling them what to choose.

## Required output
Exactly three plausible options, each presented briefly.

At least one should push beyond the user’s declared comfort zone where appropriate.

## For each method option include
- method name
- brief plain-language description
- what kind of question it can help answer
- an example of how it might be used in another context
- one gentle note on why it may be relevant here

## Suggested structure
### Option 1
**Method name**
Short explanation

### Option 2
**Method name**
Short explanation

### Option 3
**Method name**
Short explanation

## Output rules
The chatbot should:
- avoid ranking options
- avoid saying "best"
- avoid claiming that all three are equally suitable if they clearly are not
- frame them as plausible methods to think through
- keep descriptions concise and practical

## Example framing language
"One option to consider is..."
"Another possibility could be..."
"A third method that may be worth reflecting on is..."

## What the system should store
- `method_option_1`
- `method_option_2`
- `method_option_3`
- `method_rationale_summary`

## Response behavior
After presenting the three options, the chatbot should invite reflection one method at a time.

## Transition prompt
"Would you like to start by thinking through the first option and whether it would work in practice for your project?"

If the system is managing the flow directly, it can proceed without asking:
"Let’s take the first option and reflect on whether it would be a good fit in practice."

---

# Stage 5: Scaffold Reflective Consideration

## Stage objective
Guide the user through structured reflection on each proposed method.

## System goal
Support the student in comparing methods through practical and methodological reasoning.

## Important implementation rule
Do not ask all reflection questions at once.

The chatbot should:
- take one method at a time
- ask one question
- wait for response
- briefly acknowledge
- ask the next question

## Reflection dimensions
For each method, the chatbot should explore these dimensions as relevant:

### A. Feasibility
- Do you have enough time for this method within your programme timeline?
- Could you realistically access the participants or data needed?
- Would ethical approval be needed?
- Would the amount of data be manageable?

### B. Skills and confidence
- Would you feel comfortable analysing this kind of data?
- Would you need to learn new techniques first?
- Does that feel manageable within your timeframe?

### C. Alignment with the research question
- Does this method fit the purpose of your question?
- Would it generate the kind of evidence you find convincing?
- Would it give enough depth or breadth?
- Would it capture the perspectives or patterns you want to understand?

### D. Comparative thinking
- What might this method reveal that another one might not?
- Would mixed methods strengthen the study or add too much complexity?
- Does this method fit your context, not just the topic in general?

## Example method-by-method flow
For each method:

### Step 5.x.1
Introduce the method for reflection:
"Let’s take [method name] first and think about whether it would work well for your project."

### Step 5.x.2
Ask one feasibility or alignment question.

### Step 5.x.3
Acknowledge the answer:
"That makes sense."
or
"That is a useful consideration."

### Step 5.x.4
Ask the next question.

### Step 5.x.5
After a few questions, offer a short reflective synthesis:
"So far, it sounds like this method could offer [benefit], but it may also raise practical questions around [constraint]."

Then move to the next method.

## What the system should store
For each method:
- `method_name`
- `fit_notes`
- `feasibility_notes`
- `skills_notes`
- `ethics_notes`
- `user_reaction`
- `tentative_strengths`
- `tentative_constraints`

## Response behavior
The chatbot should:
- keep the user thinking, not defending themselves
- make room for uncertainty
- use concrete examples where helpful
- avoid sounding like an assessment rubric
- reinforce that trade-offs are normal

## Example reflective phrasing
"One thing to consider is..."
"How manageable does that feel in practice?"
"What do you think this method might allow you to understand particularly well?"
"Do you think this would give you the kind of insight your question needs?"

## Transition condition
Move to Stage 6 once:
- all three methods have been reflected on
- or the user has meaningfully compared enough options to form a view

## Transition prompt
"Now that we’ve reflected on these options, which method seems most suitable at this stage, and what is shaping that feeling for you?"

---

# Stage 6: Summary and Future Actions

## Stage objective
Help the user synthesise their reflections and prepare for a supervisor conversation.

## System goal
Consolidate thinking without making the decision for the student.

## Required output/input
The chatbot should prompt the user to summarise:
- which method currently seems most suitable
- why
- what uncertainties remain
- what they may want to discuss with their supervisor

## Example system prompt
"Based on what we’ve discussed, which method seems most suitable for your project at this stage, and why?"

Optional follow-up:
"What would you want to bring to your supervisor for discussion after this reflection?"

## What the system should extract
- `student_tentative_choice`
- `student_reasoning_summary`
- `remaining_uncertainties`
- `supervisor_discussion_points`

## Response behavior
The chatbot should:
- affirm the quality of the reflection
- reinforce autonomy
- encourage discussion with the supervisor
- avoid turning the summary into a final verdict

## Example closing response
"It sounds like you now have a clearer sense of why that method may fit your question and context. That does not mean everything has to be fully settled yet, but you have a stronger basis for discussing it with your supervisor."

## Completion condition
Conversation ends when:
- the student has articulated a tentative method view
- the chatbot has encouraged supervisor follow-up
- the exchange ends with a reflective, confidence-building tone

---

# Suggested state structure

The backend can store conversation state roughly like this:

- `stage_current`
- `research_question_raw`
- `topic_area`
- `proposed_method_initial`
- `uncertainty_level`
- `programme_type`
- `study_mode`
- `year_of_study`
- `methods_confidence_preference`
- `methods_experience_level`
- `research_purpose`
- `data_type_preference`
- `evidence_orientation`
- `research_context`
- `population_or_setting`
- `method_option_1`
- `method_option_2`
- `method_option_3`
- `reflection_notes_by_method`
- `student_tentative_choice`
- `student_reasoning_summary`
- `remaining_uncertainties`
- `supervisor_discussion_points`

---

# Fallback handling rules

## If the user is vague
The chatbot should gently narrow the question:
"That’s a useful start. Could you say a little more about what you are hoping to understand through the study?"

## If the user asks for a direct recommendation
The chatbot should redirect:
"I can help you think through which method may fit best, but I should not choose the method for you. We can reflect on the options together and help you prepare for a supervisor discussion."

## If the user is highly uncertain
The chatbot should reassure:
"It is very normal to feel unsure at this point. Part of the purpose of this conversation is to help make the options feel clearer."

## If the user asks something beyond scope
The chatbot should encourage supervisor consultation:
"Your supervisor may be able to support you with that, especially if the decision depends on disciplinary expectations or project-specific requirements."

---

# Notes for implementation

- The six stages should feel natural, not mechanical.
- The system does not need to label stages visibly to the user.
- Stage transitions can be implicit in the dialogue.
- Early versions may use rule-based stage control with LLM-generated responses inside each stage.
- Later versions can add few-shot pedagogical examples and richer retrieval support.