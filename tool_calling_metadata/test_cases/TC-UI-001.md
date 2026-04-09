---
test_case_id: TC-UI-001
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-08'
---
# TC-UI-001: Tool Calling filter appears in left navigation menu

**Objective**: Verify the 'Tool Calling' task filter is available in the RHOAI catalog's left-hand side navigation menu.

**Preconditions**:
- RHOAI UI is accessible with Model Catalog enabled
- At least one tool-calling model has been ingested into the catalog

**Test Steps**:
1. Navigate to the RHOAI Model Catalog page
2. Inspect the left-hand side filter/navigation menu
3. Verify 'Tool Calling' appears as a selectable task filter option
4. Verify 'Tool Calling' is listed alongside other existing task filters

**Expected Results**:
- 'Tool Calling' is visible as a task option in the left navigation filter menu
- The filter option is selectable/clickable
- The filter option displays the correct label ("Tool Calling")
- The filter integrates with the existing task filter design (consistent styling and placement)

**Notes**: To be filled later in the process.
