# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel
from .field_info import FieldInfo
from .enum_type_info import EnumTypeInfo

__all__ = ["ContractGetSchemaResponse", "Scope"]


class Scope(BaseModel):
    """Information about a scope (computation unit) in the contract."""

    inputs: List[FieldInfo]
    """Input fields required to run this scope"""

    internals: List[FieldInfo]
    """Internal fields used within the scope"""

    is_runnable: bool
    """
    True if this scope can be executed directly (has outputs and is not a helper
    subscope)
    """

    name: str
    """The scope name as defined in the specification"""

    outputs: List[FieldInfo]
    """Output fields produced by this scope"""


class ContractGetSchemaResponse(BaseModel):
    """Complete schema for a contract including all scopes and types."""

    contract_id: str
    """The unique contract identifier"""

    enum_types: List[EnumTypeInfo]
    """All enum types used in the contract"""

    scopes: List[Scope]
    """All scopes defined in the contract"""

    struct_types: List["StructTypeInfo"]
    """All struct types used in the contract"""

    contract_title: Optional[str] = None
    """Human-readable contract title"""

    main_output_var: Optional[str] = None
    """The primary output variable name"""

    main_scope: Optional[str] = None
    """The primary computation scope name"""


from .struct_type_info import StructTypeInfo
