# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContractTestDataWithPreviewParams"]


class ContractTestDataWithPreviewParams(TypedDict, total=False):
    preview_model_code: Required[str]
    """The preview specification code to evaluate"""
