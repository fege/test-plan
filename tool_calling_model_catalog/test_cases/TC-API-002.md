---
test_case_id: TC-API-002
strat_key: RHAISTRAT-1262
priority: P0
status: Automated
automation_status: Complete
last_updated: '2026-04-17'
---
# TC-API-002: Verify JSON response structure includes all required tool-calling fields

**Objective**: Verify that the BFF API response schema for tool-calling models includes all required fields in the correct structure parseable by the RHOAI Serving UI.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog BFF API deployed
- Multiple validated tool-calling models ingested with different metadata values

**Test Steps**:
1. Send a GET request for the granite-3.1-8b-instruct model
2. Validate the response against the expected JSON schema:
   - `tool_calling_supported` must be a boolean
   - `required_cli_args` must be an array of strings
   - `chat_template_path` must be a string
   - `chat_template_file_name` must be a string
   - `tool_call_parser` must be a string
3. Repeat for the llama-3.3-70b-instruct model
4. Verify both responses follow the same schema structure
5. Verify field names are consistent (no camelCase vs snake_case inconsistencies)

**Expected Results**:
- All responses follow the same JSON schema
- Field names use snake_case consistently
- Field types are consistent across different models
- The structure is suitable for direct consumption by the RHOAI Serving UI

**Notes**: To be filled later in the process.
