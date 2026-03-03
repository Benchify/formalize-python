# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ContractExportParams"]


class ContractExportParams(TypedDict, total=False):
    format: str
    """Export format: 'docx' or 'pdf'"""

    include_pending: bool
    """If true, also include PENDING redlines (as tracked changes)"""
