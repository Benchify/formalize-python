# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ContractUpdateMetadataResponse"]


class ContractUpdateMetadataResponse(BaseModel):
    """Response after updating contract metadata."""

    contract_id: str
    """The updated contract's ID"""

    filename: str
    """The current filename"""

    success: bool
    """Whether the update succeeded"""

    updated_at: datetime
    """Timestamp of the update"""

    document_title: Optional[str] = None
    """The updated document title"""
