# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["StructTypeInfo"]


class StructTypeInfo(BaseModel):
    """Definition of a struct type used in the contract."""

    fields: List["StructFieldInfo"]
    """List of fields in this struct, with nested type definitions for complex types"""

    name: str
    """The struct type name"""

    kind: Optional[Literal["struct"]] = None
    """Type discriminator"""


from .struct_field_info import StructFieldInfo
