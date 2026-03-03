# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ContractWorkingCopyResponse"]


class ContractWorkingCopyResponse(BaseModel):
    """Result of generating a working copy with selected redlines."""

    errors: List[str]

    latency_seconds: float

    original_catala: str

    redlines_applied: List[str]

    redlines_failed: List[str]

    success: bool

    working_copy_catala: str
