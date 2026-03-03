# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetUploadParams"]


class DatasetUploadParams(TypedDict, total=False):
    file_base64: Required[str]
    """Base64-encoded content of the Excel (.xlsx) or CSV file"""

    filename: Required[str]
    """Original filename of the file"""

    name: Required[str]
    """User-friendly name for the dataset"""

    description: Optional[str]
    """Optional description of what this dataset tests"""

    is_primary: bool
    """Set as the primary/default dataset for this contract"""
