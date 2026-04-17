---
test_case_id: TC-API-001
strat_key: RHAISTRAT-1262
priority: P0
status: Automated
automation_status: Complete
last_updated: '2026-04-17'
---
# TC-API-001: Retrieve tool-calling metadata for a validated model via BFF API

**Objective**: Verify that the Model Catalog BFF API returns the complete tool-calling metadata for a validated model in structured JSON format.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog BFF API deployed
- At least one validated tool-calling model ingested (e.g., granite-3.1-8b-instruct)

**Test Steps**:
1. Send a GET request to the Model Catalog BFF API for the granite-3.1-8b-instruct model
2. Verify the HTTP response status is 200 OK
3. Parse the JSON response body
4. Verify the response contains `tool_calling_supported: true`
5. Verify the response contains `required_cli_args` as a non-empty array
6. Verify the response contains `chat_template_path` as a non-empty string
7. Verify the response contains `chat_template_file_name` as a non-empty string
8. Verify the response contains `tool_call_parser` as a non-empty string

**Expected Results**:
- Response status is 200
- JSON body includes all five tool-calling metadata fields with correct types
- Field values match the data ingested for the model

**Expected Response**:
```json
{
  "model_id": "granite-3.1-8b-instruct",
  "tool_calling_supported": true,
  "required_cli_args": ["--max-model-len", "8192", "--dtype", "float16"],
  "chat_template_path": "examples/tool_chat_template_granite.jinja",
  "chat_template_file_name": "tool_chat_template_granite.jinja",
  "tool_call_parser": "hermes"
}
```

**Notes**: To be filled later in the process.
