# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .formalization_status import FormalizationStatus

__all__ = ["ContractListParams"]


class ContractListParams(TypedDict, total=False):
    limit: int
    """Max contracts to return"""

    offset: int
    """Offset for pagination"""

    org_id: Optional[str]
    """Organization ID (defaults to default org)"""

    status: Optional[FormalizationStatus]
    """Filter by formalization status"""
