# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...._types import FileTypes

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name for the dataset"""

    file: Required[FileTypes]

    description: Optional[str]
    """Optional description"""

    is_primary: bool
    """Set as primary dataset"""

    target_scope: Optional[str]
    """Scope this dataset is designed for"""
