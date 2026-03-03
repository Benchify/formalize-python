# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["EnumTypeInfo", "Variant"]


class Variant(BaseModel):
    """Information about a variant within an enum type."""

    name: str
    """The variant name"""

    payload_type: Optional[str] = None
    """
    The payload type if this variant carries data (e.g., 'integer' for 'SomeValue
    content integer')
    """


class EnumTypeInfo(BaseModel):
    """Definition of an enum type used in the contract."""

    name: str
    """The enum type name"""

    variants: List[Variant]
    """List of possible enum variants"""

    kind: Optional[Literal["enum"]] = None
    """Type discriminator"""
