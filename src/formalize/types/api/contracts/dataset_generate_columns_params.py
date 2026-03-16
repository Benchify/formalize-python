# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["DatasetGenerateColumnsParams"]


class DatasetGenerateColumnsParams(TypedDict, total=False):
    contract_id: Required[str]

    fields: Required[SequenceNotStr[str]]
    """List of specification field names to generate data for"""
