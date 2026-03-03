# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ContractOptimizeParams"]


class ContractOptimizeParams(TypedDict, total=False):
    analysis_concurrency: int

    num_test_inputs: int

    output_var: Optional[str]

    party_position: str

    scope_name: Optional[str]
