# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from .formalization_status import FormalizationStatus

__all__ = ["ContractListResponse", "Contract"]


class Contract(BaseModel):
    """Summary information about a contract for list views."""

    id: str
    """The unique contract identifier"""

    created_at: datetime
    """When the contract was uploaded"""

    filename: str
    """Original uploaded filename"""

    formalization_status: FormalizationStatus
    """Current formalization status"""

    scope_count: int
    """Number of scopes defined in the contract"""

    updated_at: datetime
    """When the contract was last modified"""

    document_title: Optional[str] = None
    """Extracted document title"""

    main_scope: Optional[str] = None
    """Primary computation scope name"""


class ContractListResponse(BaseModel):
    """Response for listing contracts."""

    contracts: List[Contract]
    """List of contract summaries"""

    total: int
    """Total number of contracts matching the query"""
