# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ContractDeleteResponse"]


class ContractDeleteResponse(BaseModel):
    """Response after deleting a contract."""

    contract_id: str
    """The deleted contract's ID"""

    message: str
    """Confirmation message"""

    success: bool
    """Whether the deletion succeeded"""
