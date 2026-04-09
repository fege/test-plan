---
test_case_id: TC-UI-004
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-UI-004: Modelcard does not display TC fields for non-tool-calling models

**Objective**: Verify that modelcards for models without tool-calling support do not display any tool-calling metadata sections.

**Preconditions**:
- RHOAI UI is accessible
- A model without tool-calling support exists in the catalog (e.g., granite-3.0-2b-instruct with `tool_calling_supported: false`)

**Test Steps**:
1. Navigate to the Model Catalog and open the modelcard for granite-3.0-2b-instruct
2. Inspect the modelcard for any tool-calling related sections or fields
3. Verify no tool-calling CLI arguments, template paths, or parser information is shown

**Expected Results**:
- No tool-calling section appears in the modelcard
- No CLI arguments related to tool calling are displayed
- No chat template path or tool_call_parser fields are shown
- The modelcard renders normally with all other non-TC fields intact

**Notes**: To be filled later in the process.
