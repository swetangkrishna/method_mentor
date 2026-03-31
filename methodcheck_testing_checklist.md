# MethodCheck V1 Testing Checklist

This checklist is for the first command-line prototype of MethodCheck.

It is based on the Stage 2 testing goals in the technical process and the six-stage behavior defined in Scenario A. The main focus is response appropriateness, sequencing, coherence, reflective dialogue, supportive tone, and avoidance of prohibited behaviors. fileciteturn1file0turn1file6

---

## 1. Core flow checks

### 1.1 Session starts correctly
- [ ] The CLI starts without errors.
- [ ] The welcome message explains that the tool supports reflection rather than making the final choice.
- [ ] A new session state is created.

### 1.2 Stage progression works
- [ ] The prototype moves through all six stages in order.
- [ ] The current stage updates correctly after each stage completes.
- [ ] The session ends cleanly after Stage 6.

### 1.3 Message logging works
- [ ] User messages are stored.
- [ ] Assistant messages are stored.
- [ ] Each logged message includes stage information.

---

## 2. Stage-specific checks

### 2.1 Stage 1: Initial prompt
- [ ] The chatbot asks for the research question and any initial method idea.
- [ ] It reassures the user if they are unsure.
- [ ] It does not evaluate the method too early.

### 2.2 Stage 2: Onboarding
- [ ] The chatbot asks for programme type.
- [ ] The chatbot asks for full-time or part-time status.
- [ ] The chatbot asks for year of study.
- [ ] The chatbot asks about comfort with qualitative or quantitative methods.

### 2.3 Stage 3: Clarification
- [ ] The chatbot asks whether the question is exploratory, explanatory, or evaluative.
- [ ] The chatbot asks what type of data could answer the question.
- [ ] The chatbot asks what kind of evidence the user finds convincing.
- [ ] The chatbot uses gentle clarification rather than jargon-heavy explanation.

### 2.4 Stage 4: Method options
- [ ] The chatbot presents exactly three plausible methods.
- [ ] At least one method stretches beyond the user’s comfort zone where appropriate.
- [ ] Methods are presented as options, not as rankings.
- [ ] Each method includes a plain-language explanation.

### 2.5 Stage 5: Reflective comparison
- [ ] The chatbot reflects on one method at a time.
- [ ] It asks one reflection question at a time.
- [ ] It covers feasibility and alignment.
- [ ] It acknowledges user responses before moving on.
- [ ] It does not dump all reflection questions in one block.

### 2.6 Stage 6: Summary
- [ ] The chatbot asks the user which method currently seems most suitable and why.
- [ ] The chatbot allows uncertainty to remain.
- [ ] The chatbot encourages supervisor discussion.
- [ ] The chatbot ends in a confidence-building way.

---

## 3. Dialogue quality checks

### 3.1 Appropriate responses
- [ ] Responses match what the user has said.
- [ ] The chatbot does not drift off-topic.
- [ ] The chatbot uses plain, supportive language.

### 3.2 Sequencing
- [ ] The questions follow a logical order.
- [ ] The chatbot does not skip essential clarification too early.
- [ ] The chatbot does not present methods before enough context is gathered.

### 3.3 Coherence
- [ ] The chatbot remembers earlier answers.
- [ ] Method suggestions align with the clarified research question.
- [ ] The final summary matches the prior discussion.

### 3.4 Reflective dialogue
- [ ] The chatbot prompts reasoning rather than supplying answers.
- [ ] It helps the user consider trade-offs.
- [ ] It keeps inquiry open instead of closing it down too early.

---

## 4. Prohibited behavior checks

The chatbot must not do the following. Each item should be manually checked during testing. fileciteturn1file6

- [ ] It does not choose a method for the student.
- [ ] It does not say one method is definitely best without user-led reasoning.
- [ ] It does not replace the role of the supervisor.
- [ ] It does not shame the user for uncertainty.
- [ ] It does not overwhelm the user with long, dense explanations.

---

## 5. Edge-case checks

### 5.1 Very vague user input
- [ ] The chatbot asks a narrowing follow-up question.
- [ ] It stays supportive.

### 5.2 User asks for a direct recommendation
- [ ] The chatbot refuses to choose for them.
- [ ] It redirects to reflective comparison.
- [ ] It suggests bringing the issue to the supervisor.

### 5.3 User remains unsure after reflection
- [ ] The chatbot still provides a useful summary.
- [ ] It normalises partial uncertainty.
- [ ] It encourages a supervisor discussion rather than pretending certainty.

---

## 6. Minimum test scenarios

The first manual testing round should include at least three scenarios inspired by the attached dialogue examples. fileciteturn1file1turn1file2turn1file4

### Scenario A
A user leaning toward qualitative interviews and worried that interviews may be too simple.

### Scenario B
A user unsure about method and wanting to understand parent or teacher experiences.

### Scenario C
A user interested in a large dataset and quantitative secondary analysis.

For each scenario record:
- prompt used
- method options generated
- any response problems
- any sequencing problems
- any tone problems
- whether the final summary was useful

---

## 7. Pass criteria for first prototype

The first prototype is ready for the next iteration if:
- it completes all six stages without breaking,
- it produces three plausible methods,
- it keeps a supportive reflective tone,
- it avoids prohibited behavior,
- and the final summary is useful for supervisor preparation. fileciteturn1file0turn1file6
