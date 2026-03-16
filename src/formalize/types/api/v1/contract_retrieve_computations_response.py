# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .field_info import FieldInfo

__all__ = ["ContractRetrieveComputationsResponse", "Computation"]


class Computation(BaseModel):
    """Information about a computation that can be performed on a contract."""

    description: str
    """Human-readable description of what this computes"""

    inputs: List[FieldInfo]
    """Required input fields"""

    outputs: List[FieldInfo]
    """Output fields produced"""

    required_types: List[str]
    """Names of struct/enum types needed to construct inputs"""

    scope_name: str
    """The scope name that performs this computation"""


class ContractRetrieveComputationsResponse(BaseModel):
    """Response listing all computations available for a contract."""

    computations: List[Computation]
    """List of available computations"""

    contract_id: str
    """The unique contract identifier"""

    contract_title: Optional[str] = None
    """Human-readable contract title"""
