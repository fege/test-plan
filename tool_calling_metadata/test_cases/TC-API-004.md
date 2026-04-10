---
test_case_id: TC-API-004
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-API-004: Retrieve metadata for a non-existent model returns appropriate error

**Objective**: Verify the BFF API returns a proper error response when requesting metadata for a model that does not exist in the catalog.

**Test Steps**:
1. Send a GET request to retrieve metadata for a model ID that does not exist (e.g., `nonexistent-model-v99`)
2. Verify the response status code indicates the model was not found (e.g., 404)
3. Verify the response body contains an appropriate error message

**Expected Results**:
- Response status code is 404 (Not Found)
- Response body contains a meaningful error message indicating the model was not found
- No tool-calling metadata fields are returned

**Notes**: To be filled later in the process.
