---
test_case_id: TC-FILTER-002
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-FILTER-002: Filter returns only tool-calling-enabled models

**Objective**: Verify that selecting the 'Tool Calling' filter in the catalog UI displays only models that have `tool_calling_supported: true` with validated metadata.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- Catalog contains a mix of tool-calling-enabled and non-tool-calling models (at least 3 of each)

**Test Steps**:
1. Navigate to the RHOAI Model Catalog UI
2. Note the total number of models displayed (should include both types)
3. Click the 'Tool Calling' filter in the left navigation
4. Verify the model list is filtered to show only tool-calling-enabled models
5. Verify each displayed model has a "Tool Calling" tag or indicator
6. Verify the count matches the number of models ingested with `tool_calling_supported: true`
7. Verify no models without tool-calling support appear in the filtered results

**Expected Results**:
- Only tool-calling-enabled models are displayed after filtering
- Model count is correct and matches the database count
- Non-tool-calling models are excluded from the filtered view

**Notes**: To be filled later in the process.
