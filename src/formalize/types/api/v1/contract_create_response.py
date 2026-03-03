# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .formalization_status import FormalizationStatus

__all__ = ["ContractCreateResponse"]


class ContractCreateResponse(BaseModel):
    """Response after creating a new contract."""

    contract_id: str
    """The new contract's ID"""

    created_at: datetime
    """When the contract was created"""

    filename: str
    """The stored filename"""

    formalization_status: FormalizationStatus
    """Initial formalization status"""

    success: bool
    """Whether the creation succeeded"""

    document_title: Optional[str] = None
    """The document title"""
