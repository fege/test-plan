---
feature: tool_calling_model_catalog
strat_key: RHAISTRAT-1262
status: Open
gap_count: 21
last_updated: '2026-04-13'
---
# Gaps -- Tool Calling Model Catalog

## Scope & Endpoints
- **BFF API specification** -- Exact REST API endpoint path, HTTP method, request/response schema, query parameters, error codes, and pagination are not specified. Would be resolved by: ADR / API spec
- **Ingestion pipeline interface/API contract** -- How will Model Validation team output be consumed (manual upload, automated pipeline, webhook)? File format? Would be resolved by: ADR / design doc
- **Database schema migration details (DDL, ORM models)** -- Migration scripts and ORM model definitions for the new fields are not specified. Would be resolved by: ADR / design doc
- **UI component architecture for filter and modelcard rendering** -- UI component names for the 'Tool Calling' filter and modelcard rendering are not detailed. Would be resolved by: design doc / feature refinement
- **Error handling and validation rules for metadata fields** -- Validation rules for required_cli_args list format (array of strings vs structured objects). Would be resolved by: ADR / API spec
- **Versioning and rollback strategy for metadata changes** -- How template paths will be managed across RHAIIS/ModelCar image versions. Would be resolved by: ADR / design doc
- **Authentication/authorization requirements for BFF API and ingestion pipeline** -- Specific RBAC rules for catalog ingestion and API consumption. Would be resolved by: ADR / API spec

## Test Strategy & Risks
- **Specific BFF API schema contract** -- What JSON structure will the BFF return? Which fields are required vs optional? Error response format? Would be resolved by: API spec
- **Ingestion pipeline implementation details** -- Manual upload vs automated pipeline? File format? Would be resolved by: design doc or feature refinement
- **Exact UI filter implementation** -- How does "Tool Calling" task integrate with existing left nav taxonomy? Is it a new top-level category or subcategory? Would be resolved by: feature refinement or design doc
- **Validation criteria for "Tool Calling Enabled" tag** -- What constitutes a "validated" model? Which metadata fields must be present? Who approves tagging? Would be resolved by: feature refinement
- **RHAIIS vs ModelCar image versioning strategy** -- How will template paths be managed across image versions? Is there a version mapping table? Would be resolved by: ADR

## Environment & Infrastructure
- **Model Validation team output format and handoff mechanism** -- Exact JSON/YAML structure, delivery mechanism, and update frequency. Would be resolved by: ADR or technical design doc
- **Specific RHAIIS and ModelCar version requirements** -- Pins versions compatible with RHOAI 3.4 Dev Preview. Would be resolved by: feature refinement or ADR
- **Model Catalog database schema migration strategy** -- Backward compatibility approach, rollback plan, and migration tooling. Would be resolved by: ADR
- **List of validated models from RHAISTRAT-1165** -- Specific models to be used as test data. Would be resolved by: feature refinement or external dependency tracking
- **API BFF endpoint specification for tool-calling metadata** -- Request/response schemas, query parameters for filtering, and error codes. Would be resolved by: API spec
- **Exact permission requirements for service accounts and user roles** -- RBAC rules for catalog ingestion and API consumption. Would be resolved by: design doc or ADR
- **Chat template file distribution mechanism** -- Whether templates are bundled with images, stored in ConfigMaps, or fetched dynamically. Would be resolved by: design doc
- **UI filter implementation details for 'Tool Calling' task** -- Filter placement, interaction with existing filters, and backend query mapping. Would be resolved by: design doc or UI spec
