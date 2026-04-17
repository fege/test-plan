---
test_case_id: TC-API-004
strat_key: RHAISTRAT-1262
priority: P1
status: Automated
automation_status: Complete
last_updated: '2026-04-17'
---
# TC-API-004: Retrieve metadata for model without tool-calling support

**Objective**: Verify that the BFF API returns a well-formed response for a model that does not have tool-calling support, with tool-calling fields absent or null.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog BFF API deployed
- A model ingested without tool-calling metadata (pre-existing or explicitly `tool_calling_supported: false`)

**Test Steps**:
1. Send a GET request to the BFF API for a non-tool-calling model (e.g., a text-generation-only model)
2. Verify the HTTP response status is 200 OK
3. Verify `tool_calling_supported` is `false` or absent
4. Verify `required_cli_args`, `chat_template_path`, `chat_template_file_name`, and `tool_call_parser` are null, empty, or absent
5. Verify the response does not include any tool-calling-specific fields with placeholder or default values that could be mistaken for real metadata

**Expected Results**:
- Response is valid JSON with 200 status
- Tool-calling fields are clearly absent or null, not populated with defaults
- The Serving UI can reliably determine this model does not support tool calling

**Notes**: To be filled later in the process.
