---
test_case_id: TC-FILTER-003
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-FILTER-003: Tool Calling filter combined with existing task filters

**Objective**: Verify that the 'Tool Calling' filter works correctly when combined with other existing task filters in the catalog UI.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- Catalog contains models with various task tags and some with tool-calling support

**Test Steps**:
1. Navigate to the RHOAI Model Catalog UI
2. Apply the 'Tool Calling' filter
3. Note the filtered model count
4. Apply an additional existing task filter (e.g., 'Text Generation')
5. Verify the results show only models matching BOTH filters (intersection)
6. Remove the 'Tool Calling' filter while keeping the other filter
7. Verify the results update to show all models matching only the remaining filter
8. Re-apply 'Tool Calling' and verify the combined results are consistent

**Expected Results**:
- Filters compose using AND logic (intersection of results)
- Combined filter count is less than or equal to either individual filter count
- Removing one filter correctly expands results to match the remaining filter
- No UI errors or inconsistent states when toggling filters

**Notes**: To be filled later in the process.
