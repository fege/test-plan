---
test_case_id: TC-API-007
strat_key: RHAISTRAT-1262
priority: P2
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-API-007: Request metadata for non-existent model returns appropriate error

**Objective**: Verify that the BFF API returns an appropriate error response when queried for a model that does not exist in the catalog.

**Test Steps**:
1. Send a GET request to the BFF API for a model ID that does not exist (e.g., `nonexistent-model-v99`)
2. Verify the HTTP response status is 404 Not Found
3. Verify the response body contains an error message indicating the model was not found
4. Verify the error response is valid JSON
5. Verify no sensitive internal information (stack traces, database details) is leaked in the error response

**Expected Results**:
- Response status is 404
- Error message is descriptive but safe (e.g., `{"error": "Model not found", "model_id": "nonexistent-model-v99"}`)
- No 500 Internal Server Error or unhandled exception

**Notes**: To be filled later in the process.
