# Test Case Index -- Tool Calling Model Catalog

**Test Plan**: [TestPlan.md](../TestPlan.md)
**Strategy**: [RHAISTRAT-1262](https://redhat.atlassian.net/browse/RHAISTRAT-1262)

## Quick Stats

| Metric | Count |
|--------|-------|
| Total Test Cases | 42 |
| P0 (Critical) | 19 |
| P1 (High) | 18 |
| P2 (Medium) | 5 |

## TC-SCHEMA -- Schema Enhancement and Metadata Field Validation

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-SCHEMA-001](TC-SCHEMA-001.md) | Store tool_calling_supported boolean field in Model Catalog | P0 |
| [TC-SCHEMA-002](TC-SCHEMA-002.md) | Store required_cli_args list field in Model Catalog | P0 |
| [TC-SCHEMA-003](TC-SCHEMA-003.md) | Store chat_template_path and chat_template_file_name fields | P0 |
| [TC-SCHEMA-004](TC-SCHEMA-004.md) | Store tool_call_parser string field in Model Catalog | P0 |
| [TC-SCHEMA-005](TC-SCHEMA-005.md) | Existing models without tool-calling fields remain functional after schema update | P0 |
| [TC-SCHEMA-006](TC-SCHEMA-006.md) | Schema handles empty required_cli_args list | P1 |
| [TC-SCHEMA-007](TC-SCHEMA-007.md) | Schema rejects invalid field types for tool-calling metadata | P2 |

## TC-INGEST -- Ingestion Pipeline and Data Import

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-INGEST-001](TC-INGEST-001.md) | Ingest single validated model with complete tool-calling metadata | P0 |
| [TC-INGEST-002](TC-INGEST-002.md) | Ingest batch of validated tool-calling models from RHAISTRAT-1165 | P0 |
| [TC-INGEST-003](TC-INGEST-003.md) | Verify ingested model tagged under 'Other model' category | P0 |
| [TC-INGEST-004](TC-INGEST-004.md) | Update tool-calling metadata for previously ingested model | P1 |
| [TC-INGEST-005](TC-INGEST-005.md) | Ingest model with partial tool-calling metadata | P1 |
| [TC-INGEST-006](TC-INGEST-006.md) | Reject ingestion of model with malformed metadata | P2 |

## TC-API -- BFF API Endpoint Responses and JSON Structure

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-API-001](TC-API-001.md) | Retrieve tool-calling metadata for a validated model via BFF API | P0 |
| [TC-API-002](TC-API-002.md) | Verify JSON response structure includes all required tool-calling fields | P0 |
| [TC-API-003](TC-API-003.md) | Verify --enable-auto-tool-choice flag data in API response | P0 |
| [TC-API-004](TC-API-004.md) | Retrieve metadata for model without tool-calling support | P1 |
| [TC-API-005](TC-API-005.md) | Verify upstream chat template path in API response | P1 |
| [TC-API-006](TC-API-006.md) | Verify downstream chat template path in API response | P1 |
| [TC-API-007](TC-API-007.md) | Request metadata for non-existent model returns appropriate error | P2 |

## TC-FILTER -- UI Catalog Filtering by Tool Calling Task

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-FILTER-001](TC-FILTER-001.md) | 'Tool Calling' task filter visible in left navigation menu | P0 |
| [TC-FILTER-002](TC-FILTER-002.md) | Filter returns only tool-calling-enabled models | P0 |
| [TC-FILTER-003](TC-FILTER-003.md) | Tool Calling filter combined with existing task filters | P1 |
| [TC-FILTER-004](TC-FILTER-004.md) | Tool Calling filter shows correct model count | P1 |
| [TC-FILTER-005](TC-FILTER-005.md) | Tool Calling filter with no matching models displays empty state | P2 |

## TC-CARD -- Modelcard Rendering and YAML Frontmatter Display

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-CARD-001](TC-CARD-001.md) | Modelcard displays tool-calling CLI arguments in YAML frontmatter | P1 |
| [TC-CARD-002](TC-CARD-002.md) | CLI arguments on modelcard are copy-paste friendly | P1 |
| [TC-CARD-003](TC-CARD-003.md) | Modelcard shows --enable-auto-tool-choice and --tool-call-parser flags | P1 |
| [TC-CARD-004](TC-CARD-004.md) | Modelcard without tool-calling metadata renders without errors | P1 |
| [TC-CARD-005](TC-CARD-005.md) | Modelcard displays both upstream and downstream template paths | P2 |

## TC-AUDIT -- Source of Truth Audit and Tag Validation

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-AUDIT-001](TC-AUDIT-001.md) | Model with validated catalog entry shows "Tool Calling Enabled" tag | P0 |
| [TC-AUDIT-002](TC-AUDIT-002.md) | Model without validated entry cannot display "Tool Calling Enabled" tag | P0 |
| [TC-AUDIT-003](TC-AUDIT-003.md) | Tag removed when model's validated entry is removed from catalog | P1 |
| [TC-AUDIT-004](TC-AUDIT-004.md) | Audit identifies inconsistencies between tags and catalog entries | P1 |

## TC-REG -- Regression Testing

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-REG-001](TC-REG-001.md) | Existing model search functionality unaffected by schema update | P1 |
| [TC-REG-002](TC-REG-002.md) | Existing task filters operational after adding Tool Calling filter | P1 |
| [TC-REG-003](TC-REG-003.md) | Existing modelcard display unaffected by schema changes | P1 |
| [TC-REG-004](TC-REG-004.md) | Existing BFF API responses for non-tool-calling models unchanged | P1 |

## TC-E2E -- End-to-End Scenarios

| Test Case ID | Title | Priority |
|-------------|-------|----------|
| [TC-E2E-001](TC-E2E-001.md) | Full model ingestion to API retrieval lifecycle | P0 |
| [TC-E2E-002](TC-E2E-002.md) | Model tagging audit and validation flow | P0 |
| [TC-E2E-003](TC-E2E-003.md) | Catalog discovery and modelcard viewing flow | P0 |
| [TC-E2E-004](TC-E2E-004.md) | Schema backwards compatibility with existing models | P0 |
