# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["ContractUploadAndFormalizeParams"]


class ContractUploadAndFormalizeParams(TypedDict, total=False):
    file: Required[FileTypes]

    max_prompts: Optional[int]

    org_id: Optional[str]

    side: str
