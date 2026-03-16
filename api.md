# API

## V1

Methods:

- <code title="get /api/v1/health">client.api.v1.<a href="./src/formalize/resources/api/v1/v1.py">retrieve_health</a>() -> object</code>

### Contracts

Types:

```python
from formalize.types.api.v1 import (
    EnumTypeInfo,
    FieldInfo,
    FormalizationStatus,
    StructFieldInfo,
    StructTypeInfo,
    ContractCreateResponse,
    ContractRetrieveResponse,
    ContractListResponse,
    ContractExportResponse,
    ContractRetrieveComputationsResponse,
    ContractRetrieveDependenciesResponse,
    ContractRetrieveSchemaResponse,
    ContractUpdateMetadataResponse,
)
```

Methods:

- <code title="post /api/v1/contracts">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">create</a>(\*\*<a href="src/formalize/types/api/v1/contract_create_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contract_create_response.py">ContractCreateResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/types/{type_name}">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">retrieve</a>(type_name, \*, contract_id) -> <a href="./src/formalize/types/api/v1/contract_retrieve_response.py">ContractRetrieveResponse</a></code>
- <code title="get /api/v1/contracts">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">list</a>(\*\*<a href="src/formalize/types/api/v1/contract_list_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contract_list_response.py">ContractListResponse</a></code>
- <code title="delete /api/v1/contracts/{contract_id}">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">delete</a>(contract_id) -> object</code>
- <code title="post /api/v1/contracts/{contract_id}/export">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">export</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contract_export_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contract_export_response.py">ContractExportResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/computations">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">retrieve_computations</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contract_retrieve_computations_response.py">ContractRetrieveComputationsResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/dependencies">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">retrieve_dependencies</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contract_retrieve_dependencies_response.py">ContractRetrieveDependenciesResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/schema">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">retrieve_schema</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contract_retrieve_schema_response.py">ContractRetrieveSchemaResponse</a></code>
- <code title="patch /api/v1/contracts/{contract_id}/metadata">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">update_metadata</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contract_update_metadata_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contract_update_metadata_response.py">ContractUpdateMetadataResponse</a></code>

#### Audit

Types:

```python
from formalize.types.api.v1.contracts import AuditCreateResponse, AuditBatchResponse
```

Methods:

- <code title="post /api/v1/contracts/{contract_id}/audit">client.api.v1.contracts.audit.<a href="./src/formalize/resources/api/v1/contracts/audit.py">create</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/audit_create_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/audit_create_response.py">AuditCreateResponse</a></code>
- <code title="post /api/v1/contracts/{contract_id}/audit/batch">client.api.v1.contracts.audit.<a href="./src/formalize/resources/api/v1/contracts/audit.py">batch</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/audit_batch_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/audit_batch_response.py">AuditBatchResponse</a></code>

#### Spec

Types:

```python
from formalize.types.api.v1.contracts import SpecCreateResponse, SpecListResponse
```

Methods:

- <code title="put /api/v1/contracts/{contract_id}/spec">client.api.v1.contracts.spec.<a href="./src/formalize/resources/api/v1/contracts/spec.py">create</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/spec_create_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/spec_create_response.py">SpecCreateResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/spec">client.api.v1.contracts.spec.<a href="./src/formalize/resources/api/v1/contracts/spec.py">list</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contracts/spec_list_response.py">SpecListResponse</a></code>

#### Docx

Types:

```python
from formalize.types.api.v1.contracts import DocxCreateResponse, DocxListResponse
```

Methods:

- <code title="put /api/v1/contracts/{contract_id}/docx">client.api.v1.contracts.docx.<a href="./src/formalize/resources/api/v1/contracts/docx.py">create</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/docx_create_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/docx_create_response.py">DocxCreateResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/docx">client.api.v1.contracts.docx.<a href="./src/formalize/resources/api/v1/contracts/docx.py">list</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contracts/docx_list_response.py">DocxListResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/docx/download">client.api.v1.contracts.docx.<a href="./src/formalize/resources/api/v1/contracts/docx.py">retrieve_download</a>(contract_id) -> object</code>

### Me

Types:

```python
from formalize.types.api.v1 import UserProfile, MeRetrieveOrganizationsResponse
```

Methods:

- <code title="get /api/v1/me">client.api.v1.me.<a href="./src/formalize/resources/api/v1/me.py">list</a>() -> <a href="./src/formalize/types/api/v1/user_profile.py">UserProfile</a></code>
- <code title="patch /api/v1/me">client.api.v1.me.<a href="./src/formalize/resources/api/v1/me.py">patch_all</a>(\*\*<a href="src/formalize/types/api/v1/me_patch_all_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/user_profile.py">UserProfile</a></code>
- <code title="get /api/v1/me/organizations">client.api.v1.me.<a href="./src/formalize/resources/api/v1/me.py">retrieve_organizations</a>() -> <a href="./src/formalize/types/api/v1/me_retrieve_organizations_response.py">MeRetrieveOrganizationsResponse</a></code>

### Organizations

Types:

```python
from formalize.types.api.v1 import OrganizationInfo
```

Methods:

- <code title="post /api/v1/organizations">client.api.v1.organizations.<a href="./src/formalize/resources/api/v1/organizations/organizations.py">create</a>(\*\*<a href="src/formalize/types/api/v1/organization_create_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/organization_info.py">OrganizationInfo</a></code>
- <code title="get /api/v1/organizations/{org_id}">client.api.v1.organizations.<a href="./src/formalize/resources/api/v1/organizations/organizations.py">retrieve</a>(org_id) -> <a href="./src/formalize/types/api/v1/organization_info.py">OrganizationInfo</a></code>
- <code title="patch /api/v1/organizations/{org_id}">client.api.v1.organizations.<a href="./src/formalize/resources/api/v1/organizations/organizations.py">update</a>(org_id, \*\*<a href="src/formalize/types/api/v1/organization_update_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/organization_info.py">OrganizationInfo</a></code>
- <code title="delete /api/v1/organizations/{org_id}">client.api.v1.organizations.<a href="./src/formalize/resources/api/v1/organizations/organizations.py">delete</a>(org_id) -> object</code>

#### Members

Types:

```python
from formalize.types.api.v1.organizations import OrgMemberInfo, MemberListResponse
```

Methods:

- <code title="post /api/v1/organizations/{org_id}/members">client.api.v1.organizations.members.<a href="./src/formalize/resources/api/v1/organizations/members.py">create</a>(org_id, \*\*<a href="src/formalize/types/api/v1/organizations/member_create_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/organizations/org_member_info.py">OrgMemberInfo</a></code>
- <code title="patch /api/v1/organizations/{org_id}/members/{member_id}">client.api.v1.organizations.members.<a href="./src/formalize/resources/api/v1/organizations/members.py">update</a>(member_id, \*, org_id, \*\*<a href="src/formalize/types/api/v1/organizations/member_update_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/organizations/org_member_info.py">OrgMemberInfo</a></code>
- <code title="get /api/v1/organizations/{org_id}/members">client.api.v1.organizations.members.<a href="./src/formalize/resources/api/v1/organizations/members.py">list</a>(org_id) -> <a href="./src/formalize/types/api/v1/organizations/member_list_response.py">MemberListResponse</a></code>
- <code title="delete /api/v1/organizations/{org_id}/members/{member_id}">client.api.v1.organizations.members.<a href="./src/formalize/resources/api/v1/organizations/members.py">delete</a>(member_id, \*, org_id) -> object</code>

#### APIKeys

Types:

```python
from formalize.types.api.v1.organizations import (
    APIKeyAPIKeysResponse,
    APIKeyRetrieveAPIKeysResponse,
)
```

Methods:

- <code title="delete /api/v1/organizations/{org_id}/api-keys/{key_id}">client.api.v1.organizations.api_keys.<a href="./src/formalize/resources/api/v1/organizations/api_keys.py">delete</a>(key_id, \*, org_id) -> object</code>
- <code title="post /api/v1/organizations/{org_id}/api-keys">client.api.v1.organizations.api_keys.<a href="./src/formalize/resources/api/v1/organizations/api_keys.py">api_keys</a>(org_id, \*\*<a href="src/formalize/types/api/v1/organizations/api_key_api_keys_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/organizations/api_key_api_keys_response.py">APIKeyAPIKeysResponse</a></code>
- <code title="get /api/v1/organizations/{org_id}/api-keys">client.api.v1.organizations.api_keys.<a href="./src/formalize/resources/api/v1/organizations/api_keys.py">retrieve_api_keys</a>(org_id) -> <a href="./src/formalize/types/api/v1/organizations/api_key_retrieve_api_keys_response.py">APIKeyRetrieveAPIKeysResponse</a></code>

## Contracts

Types:

```python
from formalize.types.api import (
    ContractDocumentResponse,
    DocxChange,
    ModelSection,
    ContractDiffDocxResponse,
    ContractEditDslResponse,
    ContractEditFromDocxResponse,
    ContractEditFromTextResponse,
    ContractRetrieveResponse,
    ContractRetrieveEditSuggestionsResponse,
    ContractRetrieveModelViewResponse,
    ContractRetrieveParagraphsResponse,
    ContractSaveDslResponse,
    ContractUploadAndFormalizeResponse,
    ContractValidateDslResponse,
    ContractWorkingCopyResponse,
)
```

Methods:

- <code title="get /api/contracts/{contract_id}">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve</a>(contract_id) -> <a href="./src/formalize/types/api/contract_document_response.py">ContractDocumentResponse</a></code>
- <code title="delete /api/contracts/{contract_id}">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">delete</a>(contract_id) -> object</code>
- <code title="post /api/contracts/{contract_id}/analyze-opposing">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">analyze_opposing</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_analyze_opposing_params.py">params</a>) -> object</code>
- <code title="delete /api/contracts/{contract_id}/working-copy-cache">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">delete_working_copy_cache</a>(contract_id) -> object</code>
- <code title="post /api/contracts/{contract_id}/diff-docx">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">diff_docx</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_diff_docx_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_diff_docx_response.py">ContractDiffDocxResponse</a></code>
- <code title="post /api/contracts/{contract_id}/edit-dsl">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">edit_dsl</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_edit_dsl_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_edit_dsl_response.py">ContractEditDslResponse</a></code>
- <code title="post /api/contracts/{contract_id}/edit-from-docx">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">edit_from_docx</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_edit_from_docx_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_edit_from_docx_response.py">ContractEditFromDocxResponse</a></code>
- <code title="post /api/contracts/{contract_id}/edit-from-text">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">edit_from_text</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_edit_from_text_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_edit_from_text_response.py">ContractEditFromTextResponse</a></code>
- <code title="post /api/contracts/{contract_id}/evaluate-row">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">evaluate_row</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_evaluate_row_params.py">params</a>) -> object</code>
- <code title="post /api/contracts/{contract_id}/export">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">export</a>(contract_id) -> object</code>
- <code title="post /api/contracts/{contract_id}/optimize">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">optimize</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_optimize_params.py">params</a>) -> object</code>
- <code title="post /api/contracts/{contract_id}/refresh-scope-metadata">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">refresh_scope_metadata</a>(contract_id) -> object</code>
- <code title="get /api/contracts/">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve</a>(\*\*<a href="src/formalize/types/api/contract_retrieve_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_retrieve_response.py">ContractRetrieveResponse</a></code>
- <code title="get /api/contracts/{contract_id}/docx">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_docx</a>(contract_id) -> object</code>
- <code title="get /api/contracts/{contract_id}/edit-suggestions">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_edit_suggestions</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_retrieve_edit_suggestions_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_retrieve_edit_suggestions_response.py">ContractRetrieveEditSuggestionsResponse</a></code>
- <code title="get /api/contracts/{contract_id}/html">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_html</a>(contract_id) -> object</code>
- <code title="get /api/contracts/{contract_id}/model-code">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_model_code</a>(contract_id) -> object</code>
- <code title="get /api/contracts/{contract_id}/model-view">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_model_view</a>(contract_id) -> <a href="./src/formalize/types/api/contract_retrieve_model_view_response.py">ContractRetrieveModelViewResponse</a></code>
- <code title="get /api/contracts/{contract_id}/paragraphs">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_paragraphs</a>(contract_id) -> <a href="./src/formalize/types/api/contract_retrieve_paragraphs_response.py">ContractRetrieveParagraphsResponse</a></code>
- <code title="get /api/contracts/{contract_id}/test-data-with-working-copy">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_test_data_with_working_copy</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_retrieve_test_data_with_working_copy_params.py">params</a>) -> object</code>
- <code title="post /api/contracts/{contract_id}/save-dsl">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">save_dsl</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_save_dsl_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_save_dsl_response.py">ContractSaveDslResponse</a></code>
- <code title="post /api/contracts/{contract_id}/test-data-with-preview">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">test_data_with_preview</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_test_data_with_preview_params.py">params</a>) -> object</code>
- <code title="post /api/contracts/upload">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">upload</a>(\*\*<a href="src/formalize/types/api/contract_upload_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_document_response.py">ContractDocumentResponse</a></code>
- <code title="post /api/contracts/upload-and-formalize">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">upload_and_formalize</a>(\*\*<a href="src/formalize/types/api/contract_upload_and_formalize_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_upload_and_formalize_response.py">ContractUploadAndFormalizeResponse</a></code>
- <code title="post /api/contracts/validate-dsl">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">validate_dsl</a>(\*\*<a href="src/formalize/types/api/contract_validate_dsl_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_validate_dsl_response.py">ContractValidateDslResponse</a></code>
- <code title="post /api/contracts/{contract_id}/working-copy">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">working_copy</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_working_copy_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_working_copy_response.py">ContractWorkingCopyResponse</a></code>

### Formalize

Types:

```python
from formalize.types.api.contracts import FormalizeCreateResponse
```

Methods:

- <code title="post /api/contracts/{contract_id}/formalize">client.api.contracts.formalize.<a href="./src/formalize/resources/api/contracts/formalize.py">create</a>(contract_id, \*\*<a href="src/formalize/types/api/contracts/formalize_create_params.py">params</a>) -> <a href="./src/formalize/types/api/contracts/formalize_create_response.py">FormalizeCreateResponse</a></code>
- <code title="delete /api/contracts/{contract_id}/formalize">client.api.contracts.formalize.<a href="./src/formalize/resources/api/contracts/formalize.py">delete_all</a>(contract_id) -> object</code>

### Personas

Methods:

- <code title="get /api/contracts/{contract_id}/personas">client.api.contracts.personas.<a href="./src/formalize/resources/api/contracts/personas.py">list</a>(contract_id) -> object</code>
- <code title="post /api/contracts/{contract_id}/personas/infer">client.api.contracts.personas.<a href="./src/formalize/resources/api/contracts/personas.py">infer</a>(contract_id) -> object</code>
- <code title="put /api/contracts/{contract_id}/personas/selected">client.api.contracts.personas.<a href="./src/formalize/resources/api/contracts/personas.py">update_selected</a>(contract_id, \*\*<a href="src/formalize/types/api/contracts/persona_update_selected_params.py">params</a>) -> object</code>

### Coverage

Methods:

- <code title="post /api/contracts/{contract_id}/coverage">client.api.contracts.coverage.<a href="./src/formalize/resources/api/contracts/coverage.py">create</a>(contract_id, \*\*<a href="src/formalize/types/api/contracts/coverage_create_params.py">params</a>) -> object</code>
- <code title="get /api/contracts/{contract_id}/coverage">client.api.contracts.coverage.<a href="./src/formalize/resources/api/contracts/coverage.py">list</a>(contract_id) -> object</code>
- <code title="get /api/contracts/{contract_id}/coverage/status">client.api.contracts.coverage.<a href="./src/formalize/resources/api/contracts/coverage.py">retrieve_status</a>(contract_id) -> object</code>

### Redlines

Types:

```python
from formalize.types.api.contracts import (
    ChangeType,
    RedlineResponse,
    RedlineStatus,
    RedlineUpdateRequest,
    RedlineListResponse,
)
```

Methods:

- <code title="post /api/contracts/{contract_id}/redlines">client.api.contracts.redlines.<a href="./src/formalize/resources/api/contracts/redlines.py">create</a>(contract_id, \*\*<a href="src/formalize/types/api/contracts/redline_create_params.py">params</a>) -> <a href="./src/formalize/types/api/contracts/redline_response.py">RedlineResponse</a></code>
- <code title="patch /api/contracts/{contract_id}/redlines/{redline_id}">client.api.contracts.redlines.<a href="./src/formalize/resources/api/contracts/redlines.py">update</a>(redline_id, \*, contract_id, \*\*<a href="src/formalize/types/api/contracts/redline_update_params.py">params</a>) -> <a href="./src/formalize/types/api/contracts/redline_response.py">RedlineResponse</a></code>
- <code title="get /api/contracts/{contract_id}/redlines">client.api.contracts.redlines.<a href="./src/formalize/resources/api/contracts/redlines.py">list</a>(contract_id) -> <a href="./src/formalize/types/api/contracts/redline_list_response.py">RedlineListResponse</a></code>
- <code title="delete /api/contracts/{contract_id}/redlines/{redline_id}">client.api.contracts.redlines.<a href="./src/formalize/resources/api/contracts/redlines.py">delete</a>(redline_id, \*, contract_id) -> object</code>

### OptimizationResults

Methods:

- <code title="delete /api/contracts/{contract_id}/optimization-results">client.api.contracts.optimization_results.<a href="./src/formalize/resources/api/contracts/optimization_results.py">delete_optimization_results</a>(contract_id) -> object</code>
- <code title="get /api/contracts/{contract_id}/optimization-results">client.api.contracts.optimization_results.<a href="./src/formalize/resources/api/contracts/optimization_results.py">retrieve_optimization_results</a>(contract_id) -> object</code>

### Datasets

Methods:

- <code title="post /api/contracts/{contract_id}/datasets">client.api.contracts.datasets.<a href="./src/formalize/resources/api/contracts/datasets/datasets.py">create</a>(contract_id, \*\*<a href="src/formalize/types/api/contracts/dataset_create_params.py">params</a>) -> object</code>
- <code title="get /api/contracts/{contract_id}/datasets/{dataset_id}">client.api.contracts.datasets.<a href="./src/formalize/resources/api/contracts/datasets/datasets.py">retrieve</a>(dataset_id, \*, contract_id) -> object</code>
- <code title="patch /api/contracts/{contract_id}/datasets/{dataset_id}">client.api.contracts.datasets.<a href="./src/formalize/resources/api/contracts/datasets/datasets.py">update</a>(dataset_id, \*, contract_id, \*\*<a href="src/formalize/types/api/contracts/dataset_update_params.py">params</a>) -> object</code>
- <code title="get /api/contracts/{contract_id}/datasets">client.api.contracts.datasets.<a href="./src/formalize/resources/api/contracts/datasets/datasets.py">list</a>(contract_id) -> object</code>
- <code title="delete /api/contracts/{contract_id}/datasets/{dataset_id}">client.api.contracts.datasets.<a href="./src/formalize/resources/api/contracts/datasets/datasets.py">delete</a>(dataset_id, \*, contract_id) -> object</code>
- <code title="post /api/contracts/{contract_id}/datasets/{dataset_id}/generate-columns">client.api.contracts.datasets.<a href="./src/formalize/resources/api/contracts/datasets/datasets.py">generate_columns</a>(dataset_id, \*, contract_id, \*\*<a href="src/formalize/types/api/contracts/dataset_generate_columns_params.py">params</a>) -> object</code>
- <code title="get /api/contracts/{contract_id}/datasets/{dataset_id}/download">client.api.contracts.datasets.<a href="./src/formalize/resources/api/contracts/datasets/datasets.py">retrieve_download</a>(dataset_id, \*, contract_id) -> object</code>

#### ColumnMappings

Methods:

- <code title="get /api/contracts/{contract_id}/datasets/{dataset_id}/column-mappings">client.api.contracts.datasets.column_mappings.<a href="./src/formalize/resources/api/contracts/datasets/column_mappings.py">retrieve_column_mappings</a>(dataset_id, \*, contract_id) -> object</code>
- <code title="put /api/contracts/{contract_id}/datasets/{dataset_id}/column-mappings">client.api.contracts.datasets.column_mappings.<a href="./src/formalize/resources/api/contracts/datasets/column_mappings.py">update_column_mappings</a>(dataset_id, \*, contract_id, \*\*<a href="src/formalize/types/api/contracts/datasets/column_mapping_update_column_mappings_params.py">params</a>) -> object</code>

### TestData

Methods:

- <code title="get /api/contracts/{contract_id}/test-data">client.api.contracts.test_data.<a href="./src/formalize/resources/api/contracts/test_data.py">retrieve_test_data</a>(contract_id, \*\*<a href="src/formalize/types/api/contracts/test_data_retrieve_test_data_params.py">params</a>) -> object</code>
- <code title="post /api/contracts/{contract_id}/test-data">client.api.contracts.test_data.<a href="./src/formalize/resources/api/contracts/test_data.py">test_data</a>(contract_id, \*\*<a href="src/formalize/types/api/contracts/test_data_test_data_params.py">params</a>) -> object</code>

### OutputConfigs

Methods:

- <code title="get /api/contracts/{contract_id}/output-configs">client.api.contracts.output_configs.<a href="./src/formalize/resources/api/contracts/output_configs.py">retrieve_output_configs</a>(contract_id) -> object</code>
- <code title="put /api/contracts/{contract_id}/output-configs">client.api.contracts.output_configs.<a href="./src/formalize/resources/api/contracts/output_configs.py">update_output_configs</a>(contract_id, \*\*<a href="src/formalize/types/api/contracts/output_config_update_output_configs_params.py">params</a>) -> object</code>

# Health

Methods:

- <code title="get /health">client.health.<a href="./src/formalize/resources/health.py">check</a>() -> object</code>
