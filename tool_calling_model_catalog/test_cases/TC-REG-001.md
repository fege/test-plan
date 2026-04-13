---
test_case_id: TC-REG-001
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-REG-001: Existing model search functionality unaffected by schema update

**Objective**: Verify that the Model Catalog search functionality continues to work correctly for all models after the tool-calling schema enhancement.

**Preconditions**:
- RHOAI 3.4 cluster with Model Catalog deployed
- Catalog contains both pre-existing models and newly ingested tool-calling models

**Test Steps**:
1. Search for a pre-existing model by name (e.g., "flan-t5-small") using the catalog search
2. Verify the search returns the correct result
3. Search for a tool-calling model by name (e.g., "granite-3.1-8b-instruct")
4. Verify the search returns the correct result with tool-calling metadata
5. Search using a partial name match (e.g., "granite")
6. Verify all matching models are returned regardless of tool-calling status
7. Search for a non-existent model
8. Verify the search returns an empty result without errors

**Expected Results**:
- Search results are accurate for both legacy and new models
- No performance degradation in search after schema update
- Search does not inadvertently filter by tool-calling status

**Notes**: To be filled later in the process.
