# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import api
from .. import _compat

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    api.v1.struct_field_info.StructFieldInfo.update_forward_refs()  # type: ignore
    api.v1.struct_type_info.StructTypeInfo.update_forward_refs()  # type: ignore
    api.v1.contract_retrieve_schema_response.ContractRetrieveSchemaResponse.update_forward_refs()  # type: ignore
    api.model_section.ModelSection.update_forward_refs()  # type: ignore
    api.contract_retrieve_model_view_response.ContractRetrieveModelViewResponse.update_forward_refs()  # type: ignore
else:
    api.v1.struct_field_info.StructFieldInfo.model_rebuild(_parent_namespace_depth=0)
    api.v1.struct_type_info.StructTypeInfo.model_rebuild(_parent_namespace_depth=0)
    api.v1.contract_retrieve_schema_response.ContractRetrieveSchemaResponse.model_rebuild(_parent_namespace_depth=0)
    api.model_section.ModelSection.model_rebuild(_parent_namespace_depth=0)
    api.contract_retrieve_model_view_response.ContractRetrieveModelViewResponse.model_rebuild(_parent_namespace_depth=0)
