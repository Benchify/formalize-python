# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .v1.formalization_status import FormalizationStatus

__all__ = ["ContractDocument"]


class ContractDocument(BaseModel):
    id: str

    created_at: datetime

    document_title: Optional[str] = None

    filename: str

    formalization_status: FormalizationStatus

    org_id: Optional[str] = None

    updated_at: datetime

    contract_metadata: Optional[Dict[str, object]] = None

    formalization_progress: Optional[Dict[str, object]] = None

    api_model_code: Optional[str] = FieldInfo(alias="model_code", default=None)

    optimization_results: Optional[Dict[str, object]] = None

    original_docx_path: Optional[str] = None
