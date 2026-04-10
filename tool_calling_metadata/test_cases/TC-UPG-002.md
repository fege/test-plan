---
test_case_id: TC-UPG-002
strat_key: RHAISTRAT-1262
priority: P1
status: Draft
automation_status: Not Started
last_updated: '2026-04-09'
---
# TC-UPG-002: Database schema migration completes successfully during upgrade

**Objective**: Verify that database schema migrations for tool-calling metadata fields apply cleanly during a RHOAI platform upgrade without data loss or downtime beyond the expected maintenance window.

**Preconditions**:
- RHOAI cluster with Model Catalog containing tool-calling metadata entries
- Database contains models with varying metadata completeness (some with all fields, some with tool_calling_supported=false)
- Known pre-upgrade schema version documented

**Test Steps**:
1. Document the current database schema version and tool-calling metadata table structure
2. Initiate the RHOAI platform upgrade
3. Monitor the database migration logs for errors or warnings
4. Verify the schema migration completes without errors
5. Confirm the post-upgrade schema includes all tool-calling metadata columns with correct types and constraints
6. Query the database directly to verify existing data was not altered or dropped during migration
7. Verify models with tool_calling_supported=false still have their metadata intact

**Test Data**:
- Pre-upgrade schema snapshot
- Database migration log output
- At least 2 models with complete metadata and 1 model with tool_calling_supported=false

**Expected Results**:
- Schema migration completes without errors
- All existing tool-calling metadata rows are preserved with correct values
- Column types and constraints match the expected post-upgrade schema
- No orphaned or corrupted records in the metadata tables
- Models with tool_calling_supported=false retain their original field values

**Notes**: To be filled later in the process.
