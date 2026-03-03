# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContractEditCatalaParams"]


class ContractEditCatalaParams(TypedDict, total=False):
    change_description: Required[str]

    current_catala: Optional[str]
