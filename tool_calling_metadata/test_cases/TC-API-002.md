---
test_case_id: TC-API-002
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-API-002: API response includes enable-auto-tool-choice flag context

**Objective**: Verify the BFF API response for a tool-calling model includes context about the --enable-auto-tool-choice flag required for deployment.

**Preconditions**:
- Model Catalog BFF API service is running
- A validated tool-calling model is present in the catalog

**Test Steps**:
1. Send a GET request to retrieve metadata for a validated tool-calling model
2. Verify the response includes the `--enable-auto-tool-choice` flag in the CLI arguments or as a dedicated field

**Expected Results**:
- The response contains the `--enable-auto-tool-choice` flag either within `required_cli_args` or as a separate indicator
- The flag is present for all models where `tool_calling_supported` is `true`

**Notes**: To be filled later in the process.
