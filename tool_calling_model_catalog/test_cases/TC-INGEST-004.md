---
test_case_id: TC-INGEST-004
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-INGEST-004: Update tool-calling metadata for previously ingested model

**Objective**: Verify that tool-calling metadata can be updated for a model that was previously ingested, reflecting new CLI requirements from the Model Validation team.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog deployed
- A model previously ingested with initial tool-calling metadata

**Test Steps**:
1. Confirm the existing model entry has its original tool-calling metadata (e.g., `tool_call_parser: "hermes"`)
2. Submit an update to the model's tool-calling metadata with revised values:
   - Change `tool_call_parser` from `"hermes"` to `"granite"`
   - Add a new CLI argument `"--enforce-eager"` to `required_cli_args`
   - Update `chat_template_path` to a new template version
3. Verify the update completes without errors
4. Query the catalog and confirm all updated fields reflect the new values
5. Verify the model's non-tool-calling metadata (name, description, existing tags) is unchanged

**Expected Results**:
- Updated metadata replaces previous values without creating a duplicate entry
- Non-tool-calling fields are not affected by the update
- BFF API returns the updated metadata immediately after the update

**Test Data**:
```json
{
  "model_id": "granite-3.1-8b-instruct",
  "tool_call_parser": "granite",
  "required_cli_args": ["--max-model-len", "8192", "--dtype", "float16", "--enforce-eager"],
  "chat_template_path": "examples/tool_chat_template_granite_v2.jinja",
  "chat_template_file_name": "tool_chat_template_granite_v2.jinja"
}
```

**Notes**: To be filled later in the process.
