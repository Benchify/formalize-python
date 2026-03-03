# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import TypeAlias, TypeAliasType

from ...._compat import PYDANTIC_V1
from ...._models import BaseModel
from .enum_type_info import EnumTypeInfo

__all__ = ["StructFieldInfo", "NestedType"]

if TYPE_CHECKING or not PYDANTIC_V1:
    NestedType = TypeAliasType("NestedType", Union["StructTypeInfo", EnumTypeInfo, None])
else:
    NestedType: TypeAlias = Union["StructTypeInfo", EnumTypeInfo, None]


class StructFieldInfo(BaseModel):
    """Information about a field within a struct type."""

    is_primitive: bool
    """True if this is a primitive type"""

    name: str
    """The field name"""

    type_name: str
    """The type name of this field"""

    nested_type: Optional[NestedType] = None
    """Full type definition if this field is a struct or enum (None for primitives)"""


from .struct_type_info import StructTypeInfo
