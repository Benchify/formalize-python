# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetUpdateParams"]


class DatasetUpdateParams(TypedDict, total=False):
    contract_id: Required[str]

    description: Optional[str]

    is_primary: Optional[bool]

    name: Optional[str]

    target_scope: Optional[str]
