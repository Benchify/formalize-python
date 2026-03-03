# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ContractRetrieveTestDataWithWorkingCopyParams"]


class ContractRetrieveTestDataWithWorkingCopyParams(TypedDict, total=False):
    dataset_id: Optional[str]
    """Specific dataset ID to use"""

    output_var: Optional[str]

    scope_name: Optional[str]
