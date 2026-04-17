---
test_case_id: TC-API-006
strat_key: RHAISTRAT-1262
priority: P1
status: Automated
automation_status: Complete
last_updated: '2026-04-17'
---
# TC-API-006: Verify downstream chat template path in API response

**Objective**: Verify that the BFF API correctly returns the downstream format chat template path (`opt/app-root/template/<template_file_name>`) for RHOAI deployments.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog BFF API deployed
- A model ingested with downstream chat template path format

**Test Steps**:
1. Ingest a model with `chat_template_path: "opt/app-root/template/tool_chat_template_granite.jinja"`
2. Send a GET request to the BFF API for the model
3. Verify `chat_template_path` is exactly `"opt/app-root/template/tool_chat_template_granite.jinja"`
4. Verify `chat_template_file_name` is `"tool_chat_template_granite.jinja"`
5. Verify the path prefix is `opt/app-root/template/` (downstream format)

**Expected Results**:
- Downstream path format is preserved exactly as ingested
- No path transformation or normalization is applied
- The `chat_template_file_name` is consistent with the filename portion of `chat_template_path`

**Notes**: To be filled later in the process.
