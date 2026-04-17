---
test_case_id: TC-INGEST-006
strat_key: RHAISTRAT-1262
priority: P2
status: Draft
automation_status: Not Started
last_updated: '2026-04-13'
---
# TC-INGEST-006: Reject ingestion of model with malformed metadata

**Objective**: Verify that the ingestion pipeline rejects a model entry with malformed or invalid tool-calling metadata and provides a meaningful error.

**Test Steps**:
1. Submit a model entry with malformed YAML frontmatter (e.g., invalid indentation, unclosed quotes)
2. Verify the ingestion is rejected with a parsing error
3. Submit a model entry with a `chat_template_path` containing invalid characters (e.g., `../../etc/passwd`)
4. Verify the ingestion is rejected or the path is sanitized
5. Submit a model entry with `required_cli_args` containing an extremely long string (10,000+ characters)
6. Verify the ingestion handles the boundary case appropriately

**Expected Results**:
- Malformed metadata is rejected with descriptive error messages
- Path traversal attempts in template paths are blocked
- Oversized field values are rejected or truncated with a warning
- No partial data is written to the catalog from rejected entries

**Notes**: To be filled later in the process.
