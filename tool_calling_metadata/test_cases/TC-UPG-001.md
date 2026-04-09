---
test_case_id: TC-UPG-001
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-09'
---
# TC-UPG-001: Tool-calling metadata preserved after RHOAI platform upgrade

**Objective**: Verify that all tool-calling metadata fields stored in the Model Catalog are preserved and accessible after upgrading the RHOAI platform to a new version.

**Preconditions**:
- RHOAI cluster running a version with Model Catalog and tool-calling metadata support
- Multiple models ingested with complete tool-calling metadata (tool_calling_supported, required_cli_args, chat_template_path, chat_template_file_name, tool_call_parser)
- API consumers actively retrieving tool-calling metadata

**Test Steps**:
1. Record the tool-calling metadata for all ingested models via the BFF API before upgrade
2. Perform RHOAI platform upgrade to the next supported version
3. Verify the RHOAI upgrade completes successfully and all components are running
4. Query the BFF API for each model's tool-calling metadata
5. Compare post-upgrade metadata with the pre-upgrade snapshot
6. Verify the UI still displays tool-calling fields in modelcards
7. Verify the 'Tool Calling' filter in left navigation still returns the correct models

**Test Data**:
- Pre-upgrade metadata snapshot (JSON) for at least 3 validated tool-calling models
- RHOAI upgrade target version (TBD)

**Expected Results**:
- All tool-calling metadata fields match the pre-upgrade values exactly
- No data loss or corruption in required_cli_args lists or chat_template_path strings
- BFF API responses are structurally identical before and after upgrade
- UI modelcards render tool-calling metadata correctly post-upgrade
- 'Tool Calling' filter returns the same set of models as before upgrade

**Notes**: To be filled later in the process.
