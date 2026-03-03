# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from ..formalization_status import FormalizationStatus

__all__ = ["SpecGetResponse"]


class SpecGetResponse(BaseModel):
    """Response containing the Catala specification code."""

    contract_id: str
    """The contract's ID"""

    formalization_status: FormalizationStatus
    """Current formalization status"""

    has_code: bool
    """Whether the contract has Catala code"""

    catala_code: Optional[str] = None
    """The Catala source code, or null if not yet formalized"""
