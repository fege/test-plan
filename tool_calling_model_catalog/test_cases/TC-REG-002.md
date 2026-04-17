---
test_case_id: TC-REG-002
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-REG-002: Existing task filters operational after adding Tool Calling filter

**Objective**: Verify that all pre-existing task filters in the catalog left navigation continue to function correctly after the 'Tool Calling' filter is added.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- Catalog contains models with various task assignments

**Test Steps**:
1. Navigate to the RHOAI Model Catalog UI
2. Identify all existing task filters in the left navigation (e.g., Text Generation, Text Classification, etc.)
3. Apply each existing filter one by one
4. Verify each filter returns the correct set of models
5. Verify filter counts match the actual number of models with each task
6. Verify the new 'Tool Calling' filter does not interfere with existing filters
7. Apply an existing filter and the 'Tool Calling' filter simultaneously
8. Verify the combined results are correct (intersection)

**Expected Results**:
- All pre-existing filters continue to work as before
- Filter counts are accurate
- No interference between the new 'Tool Calling' filter and existing filters
- UI layout is not broken by the addition of the new filter

**Notes**: To be filled later in the process.
