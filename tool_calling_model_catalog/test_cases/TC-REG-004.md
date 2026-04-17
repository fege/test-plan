---
test_case_id: TC-REG-004
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-REG-004: Existing BFF API responses for non-tool-calling models unchanged

**Objective**: Verify that the BFF API continues to return correct, well-formed responses for pre-existing models that do not have tool-calling metadata.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog BFF API deployed
- Pre-existing models in the catalog without tool-calling metadata

**Test Steps**:
1. Send a GET request to the BFF API for a pre-existing non-tool-calling model
2. Verify the HTTP response status is 200 OK
3. Verify the response JSON structure matches the expected schema for non-tool-calling models
4. Verify existing fields (model_id, name, description, tags) are present and correct
5. Verify the response does not include unexpected tool-calling fields with default values
6. Compare the response structure with the documented API contract from before the schema update

**Expected Results**:
- API response for legacy models is unchanged in structure and content
- No new required fields break existing API consumers
- Response is backwards compatible with existing Serving UI code

**Notes**: To be filled later in the process.
