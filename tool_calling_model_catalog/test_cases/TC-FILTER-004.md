---
test_case_id: TC-FILTER-004
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-FILTER-004: Tool Calling filter shows correct model count

**Objective**: Verify that the model count displayed alongside the 'Tool Calling' filter accurately reflects the number of tool-calling-enabled models in the catalog.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- Known quantity of tool-calling-enabled models ingested (e.g., 3 models)

**Test Steps**:
1. Navigate to the RHOAI Model Catalog UI
2. Check the model count badge next to the 'Tool Calling' filter in the left navigation
3. Verify the count matches the known number of ingested tool-calling models (3)
4. Ingest one additional tool-calling model
5. Refresh the catalog UI
6. Verify the count badge updates to reflect the new total (4)

**Expected Results**:
- Count badge accurately reflects the current number of tool-calling-enabled models
- Count updates when new models are ingested
- Count does not include models where `tool_calling_supported` is `false` or `null`

**Notes**: To be filled later in the process.
