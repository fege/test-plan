---
test_case_id: TC-API-006
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-API-006: API response is structured JSON consumable by Serving UI

**Objective**: Verify the BFF API response for tool-calling metadata uses a structured JSON format that can be parsed by the RHOAI Serving UI to pass into the Model deployments wizard.

**Preconditions**:
- Model Catalog BFF API service is running
- A validated tool-calling model is present in the catalog

**Test Steps**:
1. Send a GET request to retrieve metadata for a validated tool-calling model
2. Parse the response as JSON
3. Verify the JSON structure contains typed fields matching the expected schema
4. Verify `required_cli_args` is a proper JSON array (not a string)
5. Verify `tool_calling_supported` is a proper JSON boolean (not a string "true")

**Expected Results**:
- Response Content-Type is `application/json`
- `tool_calling_supported` is a JSON boolean
- `required_cli_args` is a JSON array of strings
- `chat_template_file_name` is a JSON string
- `chat_template_path` is a JSON string
- `tool_call_parser` is a JSON string
- No fields are serialized as incorrect types (e.g., booleans as strings)

**Notes**: To be filled later in the process.
