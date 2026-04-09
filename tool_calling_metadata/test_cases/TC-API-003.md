---
test_case_id: TC-API-003
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-API-003: Retrieve metadata for a model without tool-calling support

**Objective**: Verify the BFF API handles requests for models that do not have tool-calling metadata, returning appropriate data without tool-calling fields.

**Preconditions**:
- Model Catalog BFF API service is running
- A model without tool-calling metadata is present in the catalog (e.g., a standard text-generation model)

**Test Steps**:
1. Send a GET request to retrieve metadata for a model that does not support tool calling
2. Verify the response status code is 200
3. Verify tool-calling specific fields are either absent or indicate no support

**Expected Results**:
- Response status code is 200
- `tool_calling_supported` is `false` or the field is absent
- Tool-calling fields (`required_cli_args`, `chat_template_file_name`, `chat_template_path`, `tool_call_parser`) are either absent or null/empty

**Notes**: To be filled later in the process.
