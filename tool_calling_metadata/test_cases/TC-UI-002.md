---
test_case_id: TC-UI-002
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-UI-002: Filter by Tool Calling task shows only TC-enabled models

**Objective**: Verify that selecting the 'Tool Calling' filter in the catalog UI displays only models that support tool calling.

**Preconditions**:
- RHOAI UI is accessible
- Catalog contains both tool-calling models (e.g., granite-3.1-8b-instruct, llama-3.1-70b-instruct) and non-tool-calling models (e.g., granite-3.0-2b-instruct)

**Test Steps**:
1. Navigate to the RHOAI Model Catalog page
2. Click the 'Tool Calling' filter in the left navigation menu
3. Observe the model list updates
4. Verify only models with `tool_calling_supported: true` are displayed
5. Verify non-tool-calling models are not displayed

**Expected Results**:
- Model list updates to show only tool-calling models
- granite-3.1-8b-instruct and llama-3.1-70b-instruct appear in the filtered results
- granite-3.0-2b-instruct (non-TC) does not appear
- The filter count/badge (if present) reflects the correct number of tool-calling models

**Notes**: To be filled later in the process.
