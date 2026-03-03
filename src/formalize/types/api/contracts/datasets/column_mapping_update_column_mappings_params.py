# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ColumnMappingUpdateColumnMappingsParams"]


class ColumnMappingUpdateColumnMappingsParams(TypedDict, total=False):
    contract_id: Required[str]

    mappings: Required[Dict[str, Optional[str]]]
