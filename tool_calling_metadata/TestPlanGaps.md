---
feature: Tool Calling Metadata Integration
strat_key: RHAISTRAT-1262
status: Open
gap_count: 24
last_updated: '2026-04-09'
---
# Gaps — Tool Calling Metadata Integration

## Scope & Endpoints

- **No concrete API endpoint paths or HTTP methods specified** — would be resolved by: **ADR or API specification document**
- **No database schema details (table structure, column types, constraints, indexes)** — would be resolved by: **ADR or database design document**
- **No authentication/authorization mechanism defined for API endpoints** — would be resolved by: **ADR or security design document**
- **No error handling specifications for ingestion pipeline failures** — would be resolved by: **ADR or technical design document**
- **No validation rules for metadata fields (e.g., required_cli_args format, chat_template_path validation)** — would be resolved by: **ADR or API specification**
- **No versioning strategy details for managing metadata schema evolution** — would be resolved by: **ADR**
- **No performance requirements (API response times, concurrent ingestion capacity)** — would be resolved by: **ADR or performance requirements document**
- **No rollback/migration strategy if schema changes cause breaking changes** — would be resolved by: **ADR**
- **UI component implementation details not specified (React components, API integration points)** — would be resolved by: **Design document or UI specification** (Note: UI implementation is out of scope but interface contract is needed)

## Test Strategy & Risks

- **Detailed API specification for Model Catalog BFF endpoints** — would be resolved by: **API spec**
- **Schema definition for tool-calling metadata fields (exact field names, types, constraints beyond the proposed format)** — would be resolved by: **ADR**
- **Handoff contract and data format from Model Validation team's testing suite** — would be resolved by: **API spec / design doc**
- **Integration points and data flow between catalog ingestion pipeline and Model Validation team's output** — would be resolved by: **ADR / design doc**
- **Versioning strategy for metadata when RHAIIS/ModelCar images evolve** — would be resolved by: **ADR**
- **Backwards compatibility approach for existing API consumers during schema extension** — would be resolved by: **ADR**

## Environment & Infrastructure

- **OpenShift and RHOAI version requirements not specified** — would be resolved by: **feature refinement / design doc**
- **Specific database type and version for Model Catalog not specified** — would be resolved by: **ADR / design doc**
- ~~**RBAC role definitions for Model Catalog write access not defined**~~ — resolved: RBAC follows the same Model Registry RBAC model (per PR #5 review feedback)
- **Specific validated tool-calling model names and versions from RHAISTRAT-1165 not provided** — would be resolved by: **feature refinement**
- **Model Validation team API/integration specification not provided** — would be resolved by: **API spec / design doc**
- **Chat template storage location and access patterns not specified** — would be resolved by: **ADR / design doc**
- **Complete Model Catalog BFF API schema with tool-calling fields not provided** — would be resolved by: **API spec**
- **Ingestion pipeline architecture and workflow details not specified** — would be resolved by: **ADR / design doc**
- **RHAIIS and ModelCar container image versions not specified** — would be resolved by: **feature refinement**
- **Performance requirements for catalog queries with new metadata not specified** — would be resolved by: **feature refinement / design doc**

## Test Case Coverage Gaps

No coverage gaps identified. All 7 endpoints from Section 4 have at least one test case, all 7 test objectives from Section 1.3 are addressed, and all P0 endpoints have P0 test cases.
