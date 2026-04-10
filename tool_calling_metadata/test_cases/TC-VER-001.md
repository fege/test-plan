---
test_case_id: TC-VER-001
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-VER-001: Update chat template path for new RHAIIS version

**Objective**: Verify the catalog correctly handles metadata updates when a new RHAIIS version changes the chat template path for a model.

**Preconditions**:
- A model exists in the catalog with tool-calling metadata referencing a specific chat template path
- A simulated RHAIIS version update changes the template location

**Test Steps**:
1. Confirm the existing model entry has chat_template_path set to `/opt/app-root/template/tool_chat_template_granite.jinja`
2. Submit an update via the ingestion pipeline with the new chat template path for the updated RHAIIS version
3. Verify the catalog entry is updated with the new path
4. Verify the API returns the updated path
5. Verify the modelcard displays the updated path

**Test Data**:
```json
{
  "model_name": "granite-3.1-8b-instruct",
  "model_version": "1.0",
  "chat_template_file_name": "tool_chat_template_granite_v2.jinja",
  "chat_template_path": "/opt/app-root/template/v2/tool_chat_template_granite_v2.jinja"
}
```

**Expected Results**:
- The catalog entry reflects the updated chat template path
- The BFF API returns the new path in its response
- The modelcard displays the updated path for copy/paste
- No stale path values remain accessible

**Notes**: To be filled later in the process.
