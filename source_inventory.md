# Source Inventory

## Purpose of this document

This document records the source files currently available for the MethodCheck prototype and explains how each source should be used.

It supports:
- project scoping
- prompt design
- conversation design
- pedagogy alignment
- testing preparation
- future RAG preparation

It also helps separate:
- implementation sources
- style/example sources
- pedagogical sources
- broader project planning sources

---

# 1. Source groups overview

The current source set can be grouped into four categories:

## A. Project planning and technical scope
Used to define:
- prototype scope
- technical architecture
- project staging
- longer-term goals

## B. Scenario specification
Used to define:
- user profile
- scenario goals
- six-stage conversation flow
- functional dialogue requirements
- prohibited behaviours

## C. Dialogue exemplars
Used to define:
- tone
- pacing
- supervisory style
- reflective questioning patterns
- confidence-building language

## D. Pedagogical and conceptual grounding
Used to define:
- pedagogical rationale
- dialogic approach
- self-efficacy support
- reflective and scaffolding principles
- research methods teaching challenges

---

# 2. File-by-file inventory

## 2.1 MethodCheck Technical Process March 2026
### File role
Primary Stage 1 technical planning source.

### Main uses
- defines prototype goal
- defines technical stack
- defines four development stages
- defines immediate short-term actions
- confirms that Stage 1 is backend-first and Stage 2 is CLI testing

### Use for
- `requirements_v1.md`
- technical architecture notes
- sprint planning
- implementation sequencing
- deciding what is in scope for Version 1

### Do not use for
- detailed prompt wording
- pedagogical dialogue style
- research-method content generation

### Priority level
High

### Notes
This is the key file for deciding where to start and what the first version should include. It confirms use of LLaMA 3, Django, React, PostgreSQL, Docker, and ADAPT servers, and it makes clear that no frontend is required initially.  [oai_citation:0‡MethodCheck Technical Process March 2026.docx](sediment://file_0000000075dc7243abd13426fe59b76a)

---

## 2.2 Scenario A: MethodCheck
### File role
Primary behavior and conversation specification source.

### Main uses
- defines user profile
- defines scenario brief
- defines goals of the chatbot
- defines the six conversation stages
- provides example onboarding and clarification prompts
- defines reflective comparison expectations
- defines prohibited behaviours
- defines tone expectations such as reassurance and confidence support

### Use for
- `requirements_v1.md`
- `conversation_stages.md`
- `prompt_rules.md`
- backend conversation logic
- CLI flow design
- testing criteria

### Do not use for
- direct model training on the appendix quotes
- overly literal turn-by-turn scripting without adaptation

### Priority level
Very high

### Notes
This is the single most important implementation source for the prototype. It should be treated as the authoritative source for the six-stage flow and chatbot constraints.  [oai_citation:1‡Scenario A.docx](sediment://file_00000000ebd4724395bd341ec3c67a2f)

---

## 2.3 Scenario A Dialogue 1
### File role
Dialogue exemplar.

### Main uses
- shows reflective supervisor-style conversation
- shows supportive handling of student uncertainty
- shows exploration of alternatives without forcing a decision
- shows pacing of questions
- shows confidence-building language

### Use for
- tone design
- prompt style
- dialogue pacing
- example few-shot patterns later
- testing the chatbot against target interaction style

### Do not use for
- rigid copying of wording
- treating as formal scenario requirements

### Priority level
High

### Notes
Useful for learning how the chatbot should sound when helping a student think through a method choice in a calm, exploratory way.  [oai_citation:2‡Scenario A Dialogue 2.docx](sediment://file_0000000075187243b6d1c1a8617a02aa)

---

## 2.4 Scenario A Dialogue 2
### File role
Dialogue exemplar.

### Main uses
- shows exploratory questioning for a student considering large datasets
- shows clarification of research purpose
- shows movement from topic to evidence type
- shows balance between opportunity and feasibility
- shows gentle reflection on quantitative direction

### Use for
- style guidance
- clarification question design
- stage 3 logic inspiration
- confidence-building wording

### Do not use for
- assuming all users are quantitative
- copying dialogue verbatim as system output

### Priority level
High

### Notes
Useful for shaping how the prototype can help a student refine a question before discussing methods more concretely.  [oai_citation:3‡Scenario A Dialogue 3.docx](sediment://file_0000000053087243abe6febe7d774bc4)

---

## 2.5 Scenario A Dialogue 3
### File role
Dialogue exemplar.

### Main uses
- shows reflection on interviews, survey, observation, and mixed methods
- shows comparison of alternatives
- shows feasibility reflection
- shows reinforcement that method strength comes from alignment, not complexity
- shows how to reassure a student who thinks interviews may be “too simple”

### Use for
- stage 4 and stage 5 prompt style
- comparison logic
- reflective summaries
- supportive challenge to assumptions

### Do not use for
- direct rule extraction without reference to Scenario A
- assuming all users have similar access issues

### Priority level
High

### Notes
Particularly useful for modeling how the chatbot should compare methods without ranking them too early.  [oai_citation:4‡Scenario A Dialogue 1.docx](sediment://file_00000000af2c7243a0e8fc2a3df0121e)

---

## 2.6 D.A Narrative Review
### File role
Primary pedagogical and conceptual grounding source.

### Main uses
- explains educational chatbot landscape
- explains research methods teaching challenges
- explains dialogic pedagogy
- identifies research gaps
- proposes pedagogical alignments
- supports reflective, scaffolded, dialogic, confidence-building design
- supports use of RAG in educational chatbot contexts

### Use for
- pedagogical rationale
- tone and stance justification
- design principles
- later evaluation framework thinking
- future few-shot dialogue design
- justification of reflective rather than prescriptive behavior

### Do not use for
- direct implementation flow in place of the scenario
- overly academic wording in chatbot responses

### Priority level
Very high

### Notes
This is the main source for why the prototype should be reflective, scaffolded, dialogic, context-sensitive, and confidence-building. It also helps justify why the chatbot should not simply provide answers.  [oai_citation:5‡D.A Narrative Review.docx](sediment://file_00000000a0687243ab89efb4ba35dd69)

---

## 2.7 MethodMentor Proposal Final
### File role
Broader project scope and delivery source.

### Main uses
- defines overall project rationale
- defines project scope and objectives
- defines KPIs
- defines phases and milestones
- defines expected deliverables
- defines evaluation and scalability plans
- defines risks and mitigations

### Use for
- understanding how the prototype fits the larger project
- future planning beyond V1
- alignment with research objectives
- later evaluation planning
- project reporting

### Do not use for
- detailed Stage 1 prompt logic
- replacing the March 2026 technical process for immediate build choices

### Priority level
Medium to high

### Notes
This file is broader than the prototype build, but very useful for ensuring the prototype remains aligned with the long-term MethodMentor project and its intended evaluation pathway.  [oai_citation:6‡MethodMentor Proposal Final.docx](sediment://file_0000000063ec7246b8c1bdd3c226e4a7)

---

# 3. Source usage by task

## 3.1 For defining Version 1 scope
Use:
- MethodCheck Technical Process March 2026
- Scenario A: MethodCheck
- MethodMentor Proposal Final

Priority order:
1. Scenario A
2. Technical Process
3. Proposal Final

---

## 3.2 For designing chatbot behavior
Use:
- Scenario A: MethodCheck
- Scenario A Dialogue 1
- Scenario A Dialogue 2
- Scenario A Dialogue 3
- D.A Narrative Review

Priority order:
1. Scenario A
2. Dialogue files
3. Narrative Review

---

## 3.3 For designing tone and reflective style
Use:
- Scenario A Dialogue 1
- Scenario A Dialogue 2
- Scenario A Dialogue 3
- Scenario A: MethodCheck
- D.A Narrative Review

Priority order:
1. Dialogue files
2. Scenario A
3. Narrative Review

---

## 3.4 For later few-shot pedagogical examples
Use:
- Dialogue files
- Scenario A
- D.A Narrative Review

Notes:
The existing dialogue files are style and structure references, not enough on their own for a full few-shot bank. Later work will need more pedagogically aligned examples across all six stages.

---

## 3.5 For later RAG source preparation
Use first:
- approved open access research-methods resources from the wider project source set

Use current attached files for:
- design guidance
- conversation structure
- pedagogy guidance

Notes:
The current attached files are not yet the full research-method knowledge base. Scenario A explicitly says the domain knowledge for methods should come from open access research methods resources in another file/source set.  [oai_citation:7‡Scenario A.docx](sediment://file_00000000ebd4724395bd341ec3c67a2f)

---

# 4. Recommended implementation priority

## Tier 1: Must use immediately
- Scenario A: MethodCheck
- MethodCheck Technical Process March 2026

These define the prototype.

## Tier 2: Must use for quality
- Scenario A Dialogue 1
- Scenario A Dialogue 2
- Scenario A Dialogue 3
- D.A Narrative Review

These define how the chatbot should behave and why.

## Tier 3: Use for alignment and later planning
- MethodMentor Proposal Final

This defines where the prototype is heading in the larger project.

---

# 5. Warnings and handling notes

## 5.1 Scenario appendix quotes
The appendix quotes in Scenario A are for contextual understanding and idea grounding. They should not be treated as training material or copied into outputs.  [oai_citation:8‡Scenario A.docx](sediment://file_00000000ebd4724395bd341ec3c67a2f)

## 5.2 Dialogue files are exemplars, not strict scripts
The three dialogue files show desired style and logic, but the chatbot should not sound like it is replaying those exact conversations. It should adapt to the user’s own project context. 

## 5.3 Narrative review is for design, not direct user response
The review should shape system behavior, scaffolding, and evaluation thinking. It should not be surfaced to users in dense academic language.  [oai_citation:9‡D.A Narrative Review.docx](sediment://file_00000000a0687243ab89efb4ba35dd69)

## 5.4 Proposal is broader than the first sprint
The proposal is important for long-term alignment, but it should not distract the team from building the first command-line prototype first. 

---

# 6. Minimum documentation pack before coding

Before writing backend logic, the following documentation set should now exist:

- `requirements_v1.md`
- `conversation_stages.md`
- `prompt_rules.md`
- `source_inventory.md`

These four files are enough to begin:
- backend state design
- stage control design
- initial system prompt drafting
- CLI prototype implementation

---

# 7. Next implementation handoff

Once this inventory is complete, the next step is to convert the documents into build tasks:

## Immediate next outputs
- conversation state schema
- system prompt draft
- CLI flow pseudocode
- backend folder structure
- first sprint task list