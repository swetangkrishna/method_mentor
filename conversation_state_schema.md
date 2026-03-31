# Conversation State Schema

## Purpose of this document

This document defines the minimum conversation state required for the MethodCheck V1 prototype.

It supports:
- stage-based dialogue flow
- response generation
- reflective summaries
- CLI testing
- session logging
- future backend implementation in Django/PostgreSQL

The schema is intentionally lightweight for Version 1.

---

# 1. Design principles

The conversation state should:

- support the six-stage scenario flow
- store only what is needed for reflection and progression
- separate raw user input from interpreted fields
- allow partial completion of stages
- support iterative clarification
- make it easy to summarise the conversation at the end

For V1, the schema should be simple enough to implement with:
- one session record
- one current stage
- a small set of structured fields
- optional message history storage

---

# 2. Top-level state structure

A session can be modeled with these top-level sections:

- `session_meta`
- `stage_state`
- `user_profile`
- `research_question_state`
- `method_options_state`
- `reflection_state`
- `summary_state`
- `message_history`
- `flags`

---

# 3. Schema definition

## 3.1 session_meta

Stores technical/session information.

### Fields
- `session_id`
- `created_at`
- `updated_at`
- `status`
- `current_stage`
- `stage_completed_list`

### Notes
- `status` can be:
  - `active`
  - `completed`
  - `abandoned`
- `current_stage` should be one of:
  - `stage_1_initial`
  - `stage_2_onboarding`
  - `stage_3_clarification`
  - `stage_4_methods`
  - `stage_5_reflection`
  - `stage_6_summary`

---

## 3.2 stage_state

Stores stage-specific progress so the backend knows what question comes next.

### Fields
- `current_stage`
- `current_stage_step`
- `last_question_key`
- `awaiting_user_response`
- `stage_transition_reason`

### Example
- `current_stage = "stage_3_clarification"`
- `current_stage_step = "evidence_orientation"`
- `last_question_key = "clarification_evidence_type"`
- `awaiting_user_response = true`

### Notes
This is important because Stage 5 is sequential and method-by-method.

---

## 3.3 user_profile

Stores onboarding/background information from Stage 2.

### Fields
- `programme_type`
- `study_mode`
- `year_of_study`
- `discipline_context`
- `methods_confidence_preference`
- `methods_experience_level`

### Allowed/example values

#### `programme_type`
- `masters`
- `phd`
- `professional_doctorate`
- `other`
- `unknown`

#### `study_mode`
- `full_time`
- `part_time`
- `unknown`

#### `year_of_study`
- free text or integer
- keep flexible for V1

#### `discipline_context`
- free text
- example: `school_of_education`

#### `methods_confidence_preference`
- `qualitative`
- `quantitative`
- `mixed`
- `none`
- `unsure`

#### `methods_experience_level`
- `low`
- `medium`
- `high`
- `unknown`

### Notes
For V1, `methods_experience_level` can be inferred loosely from the user’s self-description.

---

## 3.4 research_question_state

Stores the user’s topic and clarified research framing from Stages 1 and 3.

### Fields
- `research_question_raw`
- `research_topic`
- `population_or_setting`
- `proposed_method_initial`
- `uncertainty_level`
- `research_purpose`
- `data_type_preference`
- `evidence_orientation`
- `research_context_notes`

### Allowed/example values

#### `uncertainty_level`
- `low`
- `medium`
- `high`

#### `research_purpose`
- `exploratory`
- `explanatory`
- `evaluative`
- `mixed`
- `unclear`

#### `data_type_preference`
- free text for V1
- example: `interview data`, `survey responses`, `observation notes`

#### `evidence_orientation`
- `measurable_observable`
- `experiences_meanings`
- `pragmatic_best_fit`
- `unclear`

### Notes
Keep `research_question_raw` unchanged.
Store interpreted fields separately so the system can recover if interpretation is weak.

---

## 3.5 method_options_state

Stores the three method options generated in Stage 4.

### Fields
- `generated_methods`
- `method_generation_rationale`
- `method_generation_complete`

### `generated_methods` structure
A list of exactly three method objects.

Each method object should include:
- `method_id`
- `method_name`
- `method_type`
- `description_plain`
- `relevance_reason`
- `example_context`
- `comfort_zone_relation`

### Example method object
- `method_id = "m1"`
- `method_name = "semi_structured_interviews"`
- `method_type = "qualitative"`
- `description_plain = "..."`
- `relevance_reason = "..."`
- `example_context = "..."`
- `comfort_zone_relation = "inside"` or `"outside"` or `"adjacent"`

### Allowed/example values for `method_type`
- `qualitative`
- `quantitative`
- `mixed`

### Notes
This section stores what was shown to the user so the reflection stage can refer back consistently.

---

## 3.6 reflection_state

Stores the user’s reflection on each proposed method during Stage 5.

### Fields
- `active_method_id`
- `reflection_order`
- `reflections_by_method`
- `reflection_complete`

### `reflection_order`
List of method ids in the order discussed.
Example:
- `["m1", "m2", "m3"]`

### `reflections_by_method`
Dictionary keyed by `method_id`.

Each method reflection object should include:

- `method_id`
- `reflection_started`
- `reflection_completed`
- `timeline_fit`
- `participant_access_fit`
- `analysis_skills_fit`
- `ethics_consideration`
- `data_volume_manageability`
- `research_question_alignment`
- `evidence_alignment`
- `depth_breadth_fit`
- `user_perceived_strengths`
- `user_perceived_constraints`
- `system_reflective_summary`
- `raw_reflection_notes`

### Allowed/example values for fit-style fields
For V1 use simple values:
- `good_fit`
- `possible_with_constraints`
- `unclear`
- `poor_fit`
- `not_yet_discussed`

### Notes
Do not over-automate judgment in V1.
These fields should reflect the student’s own thinking, not a hidden system verdict.

---

## 3.7 summary_state

Stores the final reflection from Stage 6.

### Fields
- `student_tentative_choice`
- `student_reasoning_summary`
- `remaining_uncertainties`
- `supervisor_discussion_points`
- `session_closing_summary`
- `summary_complete`

### Notes
`student_tentative_choice` can be:
- one method id
- a free-text method name
- `undecided`

The conversation can still be successful even if the student remains undecided but more informed.

---

## 3.8 message_history

Stores the message-level interaction history.

### Fields
A list of message objects.

Each message object:
- `message_id`
- `timestamp`
- `role`
- `stage`
- `content`
- `question_key` (optional)

### Allowed values for `role`
- `system`
- `user`
- `assistant`

### Notes
For V1, this can be stored as simple JSON or as a separate table later.

---

## 3.9 flags

Stores safety, flow, and handoff markers.

### Fields
- `needs_supervisor_redirection`
- `user_high_uncertainty`
- `question_out_of_scope`
- `requires_clarification`
- `method_choice_request_direct`
- `ethics_sensitive_topic`
- `rag_used`
- `rag_confidence_low`

### Notes
These flags help response selection and fallback handling.

---

# 4. Minimum required fields for V1

If implementation time is tight, these are the minimum fields that must exist:

## Essential
- `session_id`
- `current_stage`
- `research_question_raw`
- `proposed_method_initial`
- `programme_type`
- `study_mode`
- `year_of_study`
- `methods_confidence_preference`
- `research_purpose`
- `evidence_orientation`
- `generated_methods`
- `active_method_id`
- `reflections_by_method`
- `student_tentative_choice`
- `student_reasoning_summary`

These are enough to run a basic CLI prototype.

---

# 5. Suggested JSON-like example

## Example session object

```json
{
  "session_meta": {
    "session_id": "sess_001",
    "created_at": "2026-03-31T10:00:00Z",
    "updated_at": "2026-03-31T10:08:00Z",
    "status": "active",
    "current_stage": "stage_3_clarification",
    "stage_completed_list": ["stage_1_initial", "stage_2_onboarding"]
  },
  "stage_state": {
    "current_stage": "stage_3_clarification",
    "current_stage_step": "research_purpose",
    "last_question_key": "clarification_purpose",
    "awaiting_user_response": true,
    "stage_transition_reason": "onboarding_complete"
  },
  "user_profile": {
    "programme_type": "masters",
    "study_mode": "part_time",
    "year_of_study": "2",
    "discipline_context": "education",
    "methods_confidence_preference": "qualitative",
    "methods_experience_level": "medium"
  },
  "research_question_state": {
    "research_question_raw": "How do parents experience communication with teachers during transition to secondary school?",
    "research_topic": "parent experiences of school transition communication",
    "population_or_setting": "parents engaging with teachers during transition to secondary school",
    "proposed_method_initial": "interviews",
    "uncertainty_level": "medium",
    "research_purpose": "exploratory",
    "data_type_preference": "descriptive accounts of experiences",
    "evidence_orientation": "experiences_meanings",
    "research_context_notes": "student wants depth rather than broad patterning"
  },
  "method_options_state": {
    "generated_methods": [],
    "method_generation_rationale": "",
    "method_generation_complete": false
  },
  "reflection_state": {
    "active_method_id": null,
    "reflection_order": [],
    "reflections_by_method": {},
    "reflection_complete": false
  },
  "summary_state": {
    "student_tentative_choice": null,
    "student_reasoning_summary": "",
    "remaining_uncertainties": "",
    "supervisor_discussion_points": "",
    "session_closing_summary": "",
    "summary_complete": false
  },
  "message_history": [],
  "flags": {
    "needs_supervisor_redirection": false,
    "user_high_uncertainty": false,
    "question_out_of_scope": false,
    "requires_clarification": false,
    "method_choice_request_direct": false,
    "ethics_sensitive_topic": false,
    "rag_used": false,
    "rag_confidence_low": false
  }
}

# 6. Suggested database mapping for later Django/PostgreSQL use

## For V1, this can begin as one session object in memory or JSON.

Later, it can map to:

Table: chat_session
	•	session_id
	•	created_at
	•	updated_at
	•	status
	•	current_stage
	•	user_profile_json
	•	research_question_json
	•	method_options_json
	•	reflection_state_json
	•	summary_state_json
	•	flags_json

Table: chat_message
	•	message_id
	•	session_id
	•	timestamp
	•	role
	•	stage
	•	content
	•	question_key

This hybrid approach keeps V1 simple and still allows later normalization.

⸻

7. Implementation notes

Keep raw + interpreted values separate

Do not overwrite the user’s original wording.

Allow incomplete state

The user may stop mid-stage.

Do not encode hard judgments as truth

Store reflection as tentative and student-led.

Make Stage 5 easy to manage

This is the most state-heavy stage, so track:
	•	which method is active
	•	which question dimension is next
	•	what has already been discussed

Keep V1 flexible

It is better to store a few fields as free text than to over-engineer rigid categories too early.