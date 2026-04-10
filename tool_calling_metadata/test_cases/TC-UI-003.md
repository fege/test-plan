---
test_case_id: TC-UI-003
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-UI-003: Modelcard displays tool-calling CLI arguments and template path

**Objective**: Verify the modelcard for a tool-calling model displays the CLI arguments and chat template path so users can copy and paste them for deployment.

**Preconditions**:
- RHOAI UI is accessible
- A validated tool-calling model (e.g., granite-3.1-8b-instruct) exists in the catalog with complete metadata

**Test Steps**:
1. Navigate to the Model Catalog and open the modelcard for granite-3.1-8b-instruct
2. Locate the tool-calling section within the modelcard
3. Verify the CLI arguments are displayed (e.g., `--max-model-len 8192`)
4. Verify the chat template path is displayed (e.g., `/opt/app-root/template/tool_chat_template_granite.jinja`)
5. Verify the tool_call_parser value is displayed (e.g., `granite`)
6. Verify the `--enable-auto-tool-choice` flag is referenced

**Expected Results**:
- Tool-calling section is visible in the modelcard
- All CLI arguments from `required_cli_args` are displayed
- `chat_template_path` is displayed with the downstream path format
- `chat_template_file_name` is displayed
- `tool_call_parser` value is displayed
- The `--enable-auto-tool-choice` flag information is present
- Data is rendered from the YAML frontmatter of the modelcard

**Notes**: To be filled later in the process.
