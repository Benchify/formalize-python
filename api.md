# API

## V1

Methods:

- <code title="get /api/v1/health">client.api.v1.<a href="./src/formalize/resources/api/v1/v1.py">health_check</a>() -> object</code>

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
    ContractDeleteResponse,
    ContractExportResponse,
    ContractGetComputationsResponse,
    ContractGetDependenciesResponse,
    ContractGetSchemaResponse,
    ContractGetTypeDefinitionResponse,
    ContractUpdateMetadataResponse,
)
```

Methods:

- <code title="post /api/v1/contracts">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">create</a>(\*\*<a href="src/formalize/types/api/v1/contract_create_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contract_create_response.py">ContractCreateResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">retrieve</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contract_retrieve_response.py">ContractRetrieveResponse</a></code>
- <code title="get /api/v1/contracts">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">list</a>(\*\*<a href="src/formalize/types/api/v1/contract_list_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contract_list_response.py">ContractListResponse</a></code>
- <code title="delete /api/v1/contracts/{contract_id}">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">delete</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contract_delete_response.py">ContractDeleteResponse</a></code>
- <code title="post /api/v1/contracts/{contract_id}/export">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">export</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contract_export_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contract_export_response.py">ContractExportResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/computations">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">get_computations</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contract_get_computations_response.py">ContractGetComputationsResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/dependencies">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">get_dependencies</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contract_get_dependencies_response.py">ContractGetDependenciesResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/schema">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">get_schema</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contract_get_schema_response.py">ContractGetSchemaResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/types/{type_name}">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">get_type_definition</a>(type_name, \*, contract_id) -> <a href="./src/formalize/types/api/v1/contract_get_type_definition_response.py">ContractGetTypeDefinitionResponse</a></code>
- <code title="patch /api/v1/contracts/{contract_id}/metadata">client.api.v1.contracts.<a href="./src/formalize/resources/api/v1/contracts/contracts.py">update_metadata</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contract_update_metadata_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contract_update_metadata_response.py">ContractUpdateMetadataResponse</a></code>

#### Audit

Types:

```python
from formalize.types.api.v1.contracts import AuditRunResponse, AuditRunBatchResponse
```

Methods:

- <code title="post /api/v1/contracts/{contract_id}/audit">client.api.v1.contracts.audit.<a href="./src/formalize/resources/api/v1/contracts/audit.py">run</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/audit_run_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/audit_run_response.py">AuditRunResponse</a></code>
- <code title="post /api/v1/contracts/{contract_id}/audit/batch">client.api.v1.contracts.audit.<a href="./src/formalize/resources/api/v1/contracts/audit.py">run_batch</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/audit_run_batch_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/audit_run_batch_response.py">AuditRunBatchResponse</a></code>

#### Spec

Types:

```python
from formalize.types.api.v1.contracts import SpecUpdateResponse, SpecGetResponse
```

Methods:

- <code title="put /api/v1/contracts/{contract_id}/spec">client.api.v1.contracts.spec.<a href="./src/formalize/resources/api/v1/contracts/spec.py">update</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/spec_update_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/spec_update_response.py">SpecUpdateResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/spec">client.api.v1.contracts.spec.<a href="./src/formalize/resources/api/v1/contracts/spec.py">get</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contracts/spec_get_response.py">SpecGetResponse</a></code>

#### Docx

Types:

```python
from formalize.types.api.v1.contracts import DocxUpdateResponse, DocxGetInfoResponse
```

Methods:

- <code title="put /api/v1/contracts/{contract_id}/docx">client.api.v1.contracts.docx.<a href="./src/formalize/resources/api/v1/contracts/docx.py">update</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/docx_update_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/docx_update_response.py">DocxUpdateResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/docx/download">client.api.v1.contracts.docx.<a href="./src/formalize/resources/api/v1/contracts/docx.py">download</a>(contract_id) -> object</code>
- <code title="get /api/v1/contracts/{contract_id}/docx">client.api.v1.contracts.docx.<a href="./src/formalize/resources/api/v1/contracts/docx.py">get_info</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contracts/docx_get_info_response.py">DocxGetInfoResponse</a></code>

#### Datasets

Types:

```python
from formalize.types.api.v1.contracts import (
    TestDatasetInfo,
    DatasetUpdateResponse,
    DatasetListResponse,
    DatasetDeleteResponse,
    DatasetUploadResponse,
)
```

Methods:

- <code title="get /api/v1/contracts/{contract_id}/datasets/{dataset_id}">client.api.v1.contracts.datasets.<a href="./src/formalize/resources/api/v1/contracts/datasets.py">retrieve</a>(dataset_id, \*, contract_id) -> <a href="./src/formalize/types/api/v1/contracts/test_dataset_info.py">TestDatasetInfo</a></code>
- <code title="patch /api/v1/contracts/{contract_id}/datasets/{dataset_id}">client.api.v1.contracts.datasets.<a href="./src/formalize/resources/api/v1/contracts/datasets.py">update</a>(dataset_id, \*, contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/dataset_update_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/dataset_update_response.py">DatasetUpdateResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/datasets">client.api.v1.contracts.datasets.<a href="./src/formalize/resources/api/v1/contracts/datasets.py">list</a>(contract_id) -> <a href="./src/formalize/types/api/v1/contracts/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /api/v1/contracts/{contract_id}/datasets/{dataset_id}">client.api.v1.contracts.datasets.<a href="./src/formalize/resources/api/v1/contracts/datasets.py">delete</a>(dataset_id, \*, contract_id) -> <a href="./src/formalize/types/api/v1/contracts/dataset_delete_response.py">DatasetDeleteResponse</a></code>
- <code title="get /api/v1/contracts/{contract_id}/datasets/{dataset_id}/download">client.api.v1.contracts.datasets.<a href="./src/formalize/resources/api/v1/contracts/datasets.py">download</a>(dataset_id, \*, contract_id) -> object</code>
- <code title="post /api/v1/contracts/{contract_id}/datasets">client.api.v1.contracts.datasets.<a href="./src/formalize/resources/api/v1/contracts/datasets.py">upload</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/dataset_upload_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/dataset_upload_response.py">DatasetUploadResponse</a></code>

## Contracts

Types:

```python
from formalize.types.api import (
    ContractDocument,
    DocxChange,
    ModelSection,
    ContractListResponse,
    ContractDiffDocxResponse,
    ContractEditCatalaResponse,
    ContractEditFromDocxResponse,
    ContractEditFromTextResponse,
    ContractRetrieveEditSuggestionsResponse,
    ContractRetrieveModelViewResponse,
    ContractRetrieveParagraphsResponse,
    ContractSaveCatalaResponse,
    ContractUploadAndFormalizeResponse,
    ContractValidateCatalaResponse,
    ContractWorkingCopyResponse,
)
```

Methods:

- <code title="get /api/contracts/{contract_id}">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve</a>(contract_id) -> <a href="./src/formalize/types/api/contract_document.py">ContractDocument</a></code>
- <code title="get /api/contracts">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">list</a>(\*\*<a href="src/formalize/types/api/contract_list_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_list_response.py">ContractListResponse</a></code>
- <code title="delete /api/contracts/{contract_id}">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">delete</a>(contract_id) -> object</code>
- <code title="post /api/contracts/{contract_id}/analyze-opposing">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">analyze_opposing</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_analyze_opposing_params.py">params</a>) -> object</code>
- <code title="delete /api/contracts/{contract_id}/working-copy-cache">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">delete_working_copy_cache</a>(contract_id) -> object</code>
- <code title="post /api/contracts/{contract_id}/diff-docx">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">diff_docx</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_diff_docx_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_diff_docx_response.py">ContractDiffDocxResponse</a></code>
- <code title="post /api/contracts/{contract_id}/edit-catala">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">edit_catala</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_edit_catala_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_edit_catala_response.py">ContractEditCatalaResponse</a></code>
- <code title="post /api/contracts/{contract_id}/edit-from-docx">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">edit_from_docx</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_edit_from_docx_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_edit_from_docx_response.py">ContractEditFromDocxResponse</a></code>
- <code title="post /api/contracts/{contract_id}/edit-from-text">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">edit_from_text</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_edit_from_text_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_edit_from_text_response.py">ContractEditFromTextResponse</a></code>
- <code title="post /api/contracts/{contract_id}/evaluate-row">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">evaluate_row</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_evaluate_row_params.py">params</a>) -> object</code>
- <code title="post /api/contracts/{contract_id}/export">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">export</a>(contract_id) -> object</code>
- <code title="post /api/contracts/{contract_id}/fix-formalization">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">fix_formalization</a>(contract_id) -> object</code>
- <code title="post /api/contracts/{contract_id}/optimize">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">optimize</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_optimize_params.py">params</a>) -> object</code>
- <code title="post /api/contracts/{contract_id}/refresh-scope-metadata">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">refresh_scope_metadata</a>(contract_id) -> object</code>
- <code title="get /api/contracts/{contract_id}/catala">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_catala</a>(contract_id) -> object</code>
- <code title="get /api/contracts/{contract_id}/docx">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_docx</a>(contract_id) -> object</code>
- <code title="get /api/contracts/{contract_id}/edit-suggestions">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_edit_suggestions</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_retrieve_edit_suggestions_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_retrieve_edit_suggestions_response.py">ContractRetrieveEditSuggestionsResponse</a></code>
- <code title="get /api/contracts/{contract_id}/html">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_html</a>(contract_id) -> object</code>
- <code title="get /api/contracts/{contract_id}/model-view">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_model_view</a>(contract_id) -> <a href="./src/formalize/types/api/contract_retrieve_model_view_response.py">ContractRetrieveModelViewResponse</a></code>
- <code title="get /api/contracts/{contract_id}/paragraphs">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_paragraphs</a>(contract_id) -> <a href="./src/formalize/types/api/contract_retrieve_paragraphs_response.py">ContractRetrieveParagraphsResponse</a></code>
- <code title="get /api/contracts/{contract_id}/test-data-with-working-copy">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">retrieve_test_data_with_working_copy</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_retrieve_test_data_with_working_copy_params.py">params</a>) -> object</code>
- <code title="post /api/contracts/{contract_id}/save-catala">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">save_catala</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_save_catala_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_save_catala_response.py">ContractSaveCatalaResponse</a></code>
- <code title="post /api/contracts/{contract_id}/test-data-with-preview">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">test_data_with_preview</a>(contract_id, \*\*<a href="src/formalize/types/api/contract_test_data_with_preview_params.py">params</a>) -> object</code>
- <code title="post /api/contracts/upload">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">upload</a>(\*\*<a href="src/formalize/types/api/contract_upload_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_document.py">ContractDocument</a></code>
- <code title="post /api/contracts/upload-and-formalize">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">upload_and_formalize</a>(\*\*<a href="src/formalize/types/api/contract_upload_and_formalize_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_upload_and_formalize_response.py">ContractUploadAndFormalizeResponse</a></code>
- <code title="post /api/contracts/validate-catala">client.api.contracts.<a href="./src/formalize/resources/api/contracts/contracts.py">validate_catala</a>(\*\*<a href="src/formalize/types/api/contract_validate_catala_params.py">params</a>) -> <a href="./src/formalize/types/api/contract_validate_catala_response.py">ContractValidateCatalaResponse</a></code>
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
    RedlineUpdate,
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
