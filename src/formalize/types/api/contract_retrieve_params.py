# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ContractRetrieveParams"]


class ContractRetrieveParams(TypedDict, total=False):
    limit: int

    org_id: Optional[str]

    skip: int
