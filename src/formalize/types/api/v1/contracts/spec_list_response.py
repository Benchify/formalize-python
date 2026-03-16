# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ..formalization_status import FormalizationStatus

__all__ = ["SpecListResponse"]


class SpecListResponse(BaseModel):
    """Response containing the formal specification."""

    contract_id: str
    """The contract's ID"""

    formalization_status: FormalizationStatus
    """Current formalization status"""

    has_code: bool
    """Whether the contract has been formalized"""

    api_model_code: Optional[str] = FieldInfo(alias="model_code", default=None)
    """The specification source code, or null if not yet formalized"""
