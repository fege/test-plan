---
test_case_id: TC-FILTER-001
strat_key: RHAISTRAT-1262
priority: P0
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-FILTER-001: 'Tool Calling' task filter visible in left navigation menu

**Objective**: Verify that the 'Tool Calling' task filter appears as a selectable option in the left-hand navigation menu of the RHOAI Model Catalog UI.

**Preconditions**:
- RHOAI 3.4 cluster with RHOAI Catalog UI deployed
- At least one tool-calling-enabled model ingested into the catalog

**Test Steps**:
1. Navigate to the RHOAI Model Catalog UI in a browser
2. Locate the left-hand navigation panel with task filters
3. Verify a 'Tool Calling' option is present in the task filter list
4. Verify the filter is positioned appropriately among other task filters
5. Verify the filter displays a model count badge or indicator showing the number of tool-calling models available

**Expected Results**:
- 'Tool Calling' filter is visible and selectable in the left navigation
- Filter label is clearly readable and distinguishable from other task filters
- Filter shows correct count of tool-calling enabled models

**Notes**: To be filled later in the process.
