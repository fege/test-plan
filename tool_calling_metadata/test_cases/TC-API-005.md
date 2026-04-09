---
test_case_id: TC-API-005
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-API-005: List models filtered by Tool Calling task

**Objective**: Verify the Model Catalog API returns only models tagged with the 'Tool Calling' task when filtering by this task.

**Preconditions**:
- Model Catalog API service is running
- At least two tool-calling models and two non-tool-calling models are present in the catalog

**Test Steps**:
1. Send a request to the Model Catalog API to list models filtered by the 'Tool Calling' task
2. Verify the response status code is 200
3. Verify all returned models have the 'Tool Calling' task tag
4. Verify no non-tool-calling models appear in the results

**Expected Results**:
- Response status code is 200
- All models in the response have `tool_calling_supported: true`
- Models without tool-calling support are excluded from results
- Response includes the expected tool-calling models (e.g., granite-3.1-8b-instruct, llama-3.1-70b-instruct)

**Notes**: To be filled later in the process.
