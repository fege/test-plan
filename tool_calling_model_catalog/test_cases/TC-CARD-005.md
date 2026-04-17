---
test_case_id: TC-CARD-005
strat_key: RHAISTRAT-1262
priority: P2
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-CARD-005: Modelcard displays both upstream and downstream template paths

**Objective**: Verify that modelcards correctly display chat template paths in both upstream and downstream formats, enabling users to identify the correct path for their deployment environment.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- Models ingested with both upstream and downstream chat template path formats

**Test Steps**:
1. Navigate to the modelcard for a model with upstream template path (`examples/tool_chat_template_granite.jinja`)
2. Verify the upstream path is displayed clearly in the YAML frontmatter
3. Navigate to the modelcard for a model with downstream template path (`opt/app-root/template/tool_chat_template_granite.jinja`)
4. Verify the downstream path is displayed clearly in the YAML frontmatter
5. Verify both paths are rendered without truncation
6. Verify users can distinguish between upstream and downstream paths

**Expected Results**:
- Both path formats are fully visible without truncation
- Paths are displayed verbatim as stored in the catalog
- No path transformation or substitution occurs in the UI rendering

**Notes**: To be filled later in the process.
