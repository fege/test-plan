---
test_case_id: TC-AUDIT-003
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-AUDIT-003: Tag removed when model's validated entry is removed from catalog

**Objective**: Verify that removing or invalidating a model's tool-calling metadata from the catalog also removes the "Tool Calling Enabled" tag from the UI.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- A model currently displaying the "Tool Calling Enabled" tag with validated metadata

**Test Steps**:
1. Confirm the granite-3.1-8b-instruct model has "Tool Calling Enabled" tag in the UI
2. Remove or set `tool_calling_supported: false` for the model in the catalog
3. Refresh the RHOAI Catalog UI
4. Verify the "Tool Calling Enabled" tag is no longer displayed for the model
5. Apply the 'Tool Calling' filter and verify the model no longer appears in filtered results
6. Query the BFF API and confirm `tool_calling_supported` is now `false` or absent

**Expected Results**:
- Tag is removed from the UI after metadata is removed/invalidated
- Model no longer appears in Tool Calling filter results
- API response reflects the updated state
- No stale cached tags remain in the UI

**Notes**: To be filled later in the process.
