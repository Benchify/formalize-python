# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .enum_type_info import EnumTypeInfo

__all__ = ["ContractRetrieveResponse"]

ContractRetrieveResponse: TypeAlias = Union["StructTypeInfo", EnumTypeInfo]

from .struct_type_info import StructTypeInfo
