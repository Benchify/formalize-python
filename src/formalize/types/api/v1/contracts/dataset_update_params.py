# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetUpdateParams"]


class DatasetUpdateParams(TypedDict, total=False):
    contract_id: Required[str]

    description: Optional[str]
    """New description"""

    is_primary: Optional[bool]
    """Set as primary dataset (will unset other primary)"""

    name: Optional[str]
    """New name for the dataset"""
