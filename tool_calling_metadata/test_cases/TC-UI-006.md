---
test_case_id: TC-UI-006
strat_key: RHAISTRAT-1262
priority: P2
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-UI-006: Copy tool-calling commands from modelcard

**Objective**: Verify users can copy tool-calling CLI arguments and configuration from the modelcard for use in manual model deployment.

**Preconditions**:
- RHOAI UI is accessible
- A validated tool-calling model is present with complete metadata displayed in the modelcard

**Test Steps**:
1. Navigate to the modelcard for granite-3.1-8b-instruct
2. Locate the tool-calling metadata section
3. Select and copy the displayed CLI arguments
4. Paste into a text editor and verify the copied content matches the expected deployment arguments
5. Verify the chat template path can also be copied accurately

**Expected Results**:
- CLI arguments can be selected and copied from the modelcard
- Copied text preserves exact formatting (flags, values, paths)
- No extra whitespace, HTML tags, or formatting artifacts in the copied text
- The copied arguments are usable directly in a vLLM deployment command

**Notes**: To be filled later in the process.
