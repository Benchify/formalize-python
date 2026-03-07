# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .formalization_status import FormalizationStatus

__all__ = ["ContractRetrieveResponse"]


class ContractRetrieveResponse(BaseModel):
    """Detailed information about a single contract."""

    id: str
    """The unique contract identifier"""

    created_at: datetime
    """When the contract was uploaded"""

    filename: str
    """Original uploaded filename"""

    formalization_status: FormalizationStatus
    """Current formalization status"""

    has_model_code: bool
    """Whether the contract has been formalized"""

    has_test_data: bool
    """Whether test data has been uploaded"""

    scope_count: int
    """Number of scopes defined in the contract"""

    updated_at: datetime
    """When the contract was last modified"""

    document_title: Optional[str] = None
    """Extracted document title"""

    main_output_var: Optional[str] = None
    """Primary output variable name"""

    main_scope: Optional[str] = None
    """Primary computation scope name"""

    org_id: Optional[str] = None
    """Organization ID that owns this contract"""
