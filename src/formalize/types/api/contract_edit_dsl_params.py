# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContractEditDslParams"]


class ContractEditDslParams(TypedDict, total=False):
    change_description: Required[str]

    current_spec: Optional[str]
