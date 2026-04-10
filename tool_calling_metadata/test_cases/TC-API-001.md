---
test_case_id: TC-API-001
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-API-001: Retrieve tool-calling metadata for a validated model

**Objective**: Verify the Model Catalog BFF API returns complete tool-calling metadata in structured JSON for a validated model version.

**Preconditions**:
- Model Catalog BFF API service is running and accessible
- At least one validated tool-calling model has been ingested into the catalog (e.g., granite-3.1-8b-instruct)

**Test Steps**:
1. Send a GET request to the Model Catalog BFF API to retrieve metadata for a known validated tool-calling model
2. Verify the response status code is 200
3. Verify the response body contains all required tool-calling metadata fields

**Expected Results**:
- Response status code is 200
- Response body is valid JSON containing:
  - `tool_calling_supported` field set to `true`
  - `required_cli_args` field as a non-empty list
  - `chat_template_file_name` field as a non-empty string
  - `chat_template_path` field as a non-empty string
  - `tool_call_parser` field as a non-empty string

**Expected Response**:
```json
{
  "model_name": "granite-3.1-8b-instruct",
  "tool_calling_supported": true,
  "required_cli_args": ["--max-model-len", "8192"],
  "chat_template_file_name": "tool_chat_template_granite.jinja",
  "chat_template_path": "/opt/app-root/template/tool_chat_template_granite.jinja",
  "tool_call_parser": "granite"
}
```

**Validation**:
- Cross-check the returned metadata values against the corresponding database entry to ensure data fidelity

**Notes**: To be filled later in the process.
