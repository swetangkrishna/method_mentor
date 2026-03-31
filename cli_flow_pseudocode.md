## 7. CLI Flow Pseudocode

### Purpose of this section

This section translates the MethodCheck V1 design into a simple command-line execution flow.

It is intended to help with:
- backend implementation
- stage control
- session state handling
- test execution
- debugging the first prototype

The pseudocode is intentionally practical rather than fully abstract.

---

### 7.1 High-level CLI flow

```text
START PROGRAM
  load system prompt
  initialize empty session state
  print welcome message
  set current_stage = stage_1_initial

  LOOP until session complete or user exits
    read current stage
    generate next assistant message based on:
      - current stage
      - current stage step
      - session state
      - latest user input
      - retrieved source context if available

    print assistant message
    get user input

    if user exits:
      mark session abandoned
      save session
      END PROGRAM

    store user input in message history
    update interpreted session state
    evaluate whether current stage is complete

    if stage complete:
      transition to next stage

    if final stage complete:
      generate closing summary
      mark session completed
      save session
      END PROGRAM
END PROGRAM

7.2 Recommended CLI behavior

The CLI version should:
	•	feel conversational, not form-like
	•	show one assistant message at a time
	•	accept one user response at a time
	•	preserve session state after each turn
	•	allow graceful exit with commands like exit, quit, or stop

Optional early commands:
	•	summary → print current structured state summary
	•	state → print current stage and key fields
	•	restart → start a new session

