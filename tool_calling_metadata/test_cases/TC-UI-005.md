---
test_case_id: TC-UI-005
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-UI-005: Tool Calling Enabled tag is visible on catalog model cards

**Objective**: Verify models with validated tool-calling support display a "Tool Calling Enabled" tag or indicator in the catalog listing view.

**Preconditions**:
- RHOAI UI is accessible
- Catalog contains models both with and without tool-calling support

**Test Steps**:
1. Navigate to the Model Catalog listing page (without any filter applied)
2. Locate a tool-calling model card (e.g., granite-3.1-8b-instruct)
3. Verify it displays a "Tool Calling Enabled" tag or equivalent indicator
4. Locate a non-tool-calling model card (e.g., granite-3.0-2b-instruct)
5. Verify it does NOT display a "Tool Calling Enabled" tag

**Expected Results**:
- Tool-calling models display a visible "Tool Calling Enabled" tag in the catalog listing
- Non-tool-calling models do not display this tag
- The tag is backed by a validated entry in the catalog (not manually applied)

**Notes**: To be filled later in the process.
