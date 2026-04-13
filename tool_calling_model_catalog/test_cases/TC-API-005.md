---
test_case_id: TC-API-005
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-API-005: Verify upstream chat template path in API response

**Objective**: Verify that the BFF API correctly returns the upstream format chat template path (`examples/<template_file_name>`) for models using upstream template locations.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog BFF API deployed
- A model ingested with upstream chat template path format

**Test Steps**:
1. Ingest a model with `chat_template_path: "examples/tool_chat_template_granite.jinja"`
2. Send a GET request to the BFF API for the model
3. Verify `chat_template_path` is exactly `"examples/tool_chat_template_granite.jinja"`
4. Verify `chat_template_file_name` is `"tool_chat_template_granite.jinja"`
5. Verify the path prefix is `examples/` (upstream format)

**Expected Results**:
- Upstream path format is preserved exactly as ingested
- No path transformation or normalization is applied
- The `chat_template_file_name` is consistent with the filename portion of `chat_template_path`

**Notes**: To be filled later in the process.
