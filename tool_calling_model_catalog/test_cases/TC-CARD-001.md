---
test_case_id: TC-CARD-001
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-CARD-001: Modelcard displays tool-calling CLI arguments in YAML frontmatter

**Objective**: Verify that a modelcard for a tool-calling-enabled model displays the CLI arguments in YAML frontmatter format within the card's detail view.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- A tool-calling model ingested with complete CLI argument metadata

**Test Steps**:
1. Navigate to the RHOAI Model Catalog UI
2. Locate and click on a tool-calling-enabled model (e.g., granite-3.1-8b-instruct)
3. Open the modelcard detail view
4. Verify the YAML frontmatter section is visible on the modelcard
5. Verify the frontmatter includes `tool_calling_supported: true`
6. Verify the frontmatter includes the `required_cli_args` list
7. Verify the frontmatter includes `tool_call_parser` value
8. Verify the frontmatter includes `chat_template_path` value

**Expected Results**:
- YAML frontmatter is displayed in a readable, structured format
- All tool-calling fields are present and correctly formatted
- The content matches the metadata stored in the catalog

**Notes**: To be filled later in the process.
