# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ContractEvaluateRowParams"]


class ContractEvaluateRowParams(TypedDict, total=False):
    row_data: Required[Dict[str, object]]
    """The row data to evaluate"""

    use_working_copy: bool
    """If True, apply accepted/in-review redlines before evaluating"""
