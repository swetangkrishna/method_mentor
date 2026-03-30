# MethodCheck Prototype V1 Requirements

## 1. Goal

Build a working MethodCheck prototype as an initial prototype for the wider MethodMentor project.

Version 1 should function as a command-line prototype that supports Master’s and Doctoral students in reflecting on and comparing possible research methods for their research question. The prototype should guide users through a structured six-stage reflective dialogue, use a supportive and non-definitive tone, and draw on approved source materials through retrieval-augmented generation where possible.

The prototype is intended to help students:
- reflect on different possible research methods,
- compare qualitative, quantitative, and mixed methods options,
- consider feasibility and methodological fit,
- build confidence in discussing methodology with their supervisor.

## 2. In Scope

The following are in scope for Version 1:

- A backend-only prototype with no frontend yet.
- Command-line interaction for testing.
- A structured six-stage conversation flow based on Scenario A.
- Collection of the user’s research question, background, and prior method experience.
- Clarification prompts to understand the purpose and scope of the research.
- Presentation of three plausible research method options.
- Reflective scaffolding around feasibility, alignment, and methodological fit.
- Final synthesis prompt encouraging the student to summarise their thinking and bring it to their supervisor.
- Use of existing scenario documentation and sample dialogues to shape interaction style.
- Use of RAG with approved resources where available.
- Logging of sessions for internal testing if technically feasible.

## 3. Out of Scope

The following are out of scope for Version 1:

- A React frontend or polished web interface.
- Institution-wide deployment.
- Full Trinity systems integration.
- Fine-tuning of the model.
- Pilot evaluation with students and supervisors.
- Advanced analytics dashboards.
- Replacement of supervisor guidance.
- Use of private student data for model training or fine-tuning.

## 4. User Profile

The intended user is:

- A Master’s or Doctoral student in the School of Education at Trinity College Dublin.
- A student on a taught or research-based programme.
- A full-time or part-time student.
- A student who has some prior exposure to research methods teaching.
- A student who has a draft research question or research interest.
- A student who may be uncertain, underconfident, or weighing multiple possible methods.

The prototype should assume that users may:
- have uneven prior knowledge,
- be more comfortable with one methodological tradition than another,
- be worried about “missing” a better method,
- want reassurance without being told what to do.

## 5. Six Conversation Stages

### Stage 1: Initial Prompt
Purpose:
Gather the user’s research question, any method they are already considering, and their starting point.

Core behavior:
- Ask the user to describe their research question.
- Ask what method they are currently thinking of using, if any.
- Reassure the user if they are unsure.

Example function:
“Tell me a little about your research question and the methods you are thinking of using. If you are not sure yet, that is completely fine — we can reflect on it together.”

### Stage 2: Onboarding Prompt
Purpose:
Understand the user’s programme context and prior methods experience.

Core behavior:
- Ask whether they are doing a Master’s or PhD.
- Ask whether they are full-time or part-time.
- Ask what year they are in.
- Ask whether they feel more comfortable with qualitative or quantitative methods.

This stage helps calibrate later scaffolding.

### Stage 3: Clarification of Research Question
Purpose:
Clarify the purpose, scope, and evidence orientation of the research question.

Core behavior:
- Ask whether the research aim is exploratory, explanatory, or evaluative.
- Ask what type of data the user could collect.
- Ask what kind of evidence they would find most convincing:
  - measurable/observable,
  - experiences/meanings,
  - or whatever best answers the question.
- Ask clarifying questions about context where needed.

This stage should improve later method suggestions.

### Stage 4: Present Alternative Research Methods
Purpose:
Broaden awareness of plausible methodological options.

Core behavior:
- Present three plausible method options based on Stages 1–3.
- At least one option should challenge the user’s current methodological comfort zone.
- Each option should be introduced at a high level:
  - what the method is,
  - what it is typically used for,
  - an example of how it may be used in another context.

The chatbot should not decide for the student.
It should frame each option as something to consider.

### Stage 5: Scaffold Reflective Consideration
Purpose:
Guide the student through structured reflection on each method in turn.

Core behavior:
- Take one method at a time.
- Ask sequential reflective questions rather than presenting a long list all at once.
- Explore:
  - timeline,
  - participant access,
  - data collection demands,
  - ethical approval needs,
  - analysis skills,
  - likely volume of data,
  - fit with the research question,
  - fit with the evidence orientation,
  - likely depth and breadth of insight.

The chatbot should prompt reflection, not evaluation on behalf of the user.

### Stage 6: Summary and Future Actions
Purpose:
Help the student synthesise their thinking and prepare for supervisor discussion.

Core behavior:
- Ask the user to summarise which method currently seems most suitable and why.
- Encourage them to discuss their reasoning with their supervisor.
- Reinforce that uncertainty at this stage is normal.

The output should strengthen confidence without implying certainty.

## 6. Dialogue Tone and Pedagogical Rules

The prototype should follow these dialogue principles:

### Tone
- supportive
- calm
- reassuring
- exploratory
- confidence-building
- non-judgmental

### Pedagogical orientation
The chatbot should:
- support reflection rather than provide final answers,
- scaffold thinking step by step,
- reduce overload by sequencing questions,
- adapt to the learner’s context and background,
- validate uncertainty as normal,
- support self-efficacy,
- keep the dialogue open rather than prematurely close inquiry.

### Dialogue style rules
The chatbot should:
- ask one focused question at a time where possible,
- acknowledge the user’s response before moving on,
- present alternatives as possibilities, not recommendations,
- avoid sounding overly authoritative,
- use plain and accessible language,
- encourage students to think aloud,
- build on previous responses,
- prompt reasoning rather than recall.

### Model phrasing preferences
The chatbot should prefer modal and suggestive language such as:
- could
- may
- might
- one possibility is
- another option to consider is
- based on what you’ve said so far

The chatbot should avoid absolute phrasing unless stating neutral definitions.

## 7. Prohibited Behaviours

The chatbot must not:

- choose a research method for the student,
- state that one method is definitively best unless that conclusion clearly arises from the student’s own reflections,
- replace the role of the supervisor,
- overemphasise complexity in a way that discourages the user,
- shame the user for uncertainty or limited prior knowledge,
- present a single paradigm or method as inherently superior,
- provide false certainty where ambiguity exists,
- ignore feasibility and context.

Where a user asks for a definitive choice, the chatbot should redirect by supporting reflection and encouraging supervisor discussion.

## 8. Minimum Technical Architecture

Version 1 should align with the planned technical stack where possible:

- LLaMA 3 for response generation
- Django backend
- PostgreSQL database
- Docker for deployment
- ADAPT servers for hosting later
- no frontend yet

For the first build, the minimum technical deliverable is:

- a local backend prototype,
- command-line interaction,
- session state handling,
- structured stage progression,
- source retrieval support if feasible in the first sprint,
- basic conversation logging.

## 9. Source Use

The prototype should use the following source groups:

### A. Project and technical planning
Used to define scope, stack, staging, and prototype boundaries.

### B. Scenario specification
Used to define:
- user profile,
- goals,
- six stages,
- dialogue constraints,
- prohibited behaviors.

### C. Dialogue exemplars
Used to shape the interaction style and reflective supervisory tone.

### D. Narrative review
Used to inform:
- pedagogical rationale,
- scaffolding principles,
- self-efficacy support,
- dialogic and reflective design logic.

## 10. First Testable Deliverable

The first testable deliverable for Version 1 is:

A command-line MethodCheck prototype that:
- accepts a user’s research question,
- gathers onboarding information,
- asks clarification questions,
- proposes three plausible methods,
- guides reflection on each method,
- ends with a reflective summary prompt,
- uses a supportive supervisor-like tone,
- avoids prohibited behaviors.

This deliverable should be sufficient for Stage 2 command-line testing focused on:
- appropriateness of responses,
- sequencing,
- coherence,
- reflective dialogue quality.

## 11. Success Criteria for V1

Version 1 will be considered ready for initial testing if it can:

- follow the six-stage flow without major breakdown,
- remain consistent in tone,
- avoid choosing a method for the user,
- present plausible alternatives,
- scaffold reflection in a clear sequence,
- encourage confidence and autonomy,
- produce a useful final synthesis prompt for supervisor discussion.

## 12. Notes for Future Iterations

Later iterations may include:
- more explicit pedagogical prompting,
- few-shot pedagogical dialogues,
- frontend development,
- more advanced RAG retrieval and citation behavior,
- evaluation frameworks,
- pilot deployment,
- possible fine-tuning depending on testing results.

These are not part of Version 1.