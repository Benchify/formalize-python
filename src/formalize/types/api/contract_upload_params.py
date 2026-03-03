# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["ContractUploadParams"]


class ContractUploadParams(TypedDict, total=False):
    file: Required[FileTypes]

    org_id: Optional[str]

    side: str
