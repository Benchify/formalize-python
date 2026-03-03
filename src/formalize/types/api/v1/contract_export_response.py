# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ContractExportResponse"]


class ContractExportResponse(BaseModel):
    """Response containing export information."""

    applied_redlines: int
    """Number of redlines applied"""

    contract_id: str
    """The contract's ID"""

    download_url: str
    """URL to download the exported file"""

    filename: str
    """The exported filename"""

    format: str
    """Export format used"""

    success: bool
    """Whether export succeeded"""
