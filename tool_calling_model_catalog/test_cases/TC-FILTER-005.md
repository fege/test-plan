---
test_case_id: TC-FILTER-005
strat_key: RHAISTRAT-1262
priority: P2
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-FILTER-005: Tool Calling filter with no matching models displays empty state

**Objective**: Verify that the 'Tool Calling' filter handles the case where no tool-calling-enabled models exist in the catalog, displaying an appropriate empty state.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- No models with `tool_calling_supported: true` in the catalog (or all such models removed)

**Test Steps**:
1. Navigate to the RHOAI Model Catalog UI
2. Verify the 'Tool Calling' filter shows a count of 0 (or is hidden if designed to hide when empty)
3. If the filter is visible, click it
4. Verify an appropriate empty state message is displayed (e.g., "No models available for this filter")
5. Verify no error messages or broken UI elements appear

**Expected Results**:
- Empty state is handled gracefully with a user-friendly message
- No JavaScript errors or broken layouts
- User can easily navigate back or clear the filter

**Notes**: To be filled later in the process.
