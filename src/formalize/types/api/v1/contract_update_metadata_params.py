# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["ContractUpdateMetadataParams"]


class ContractUpdateMetadataParams(TypedDict, total=False):
    contract_metadata: Optional[Dict[str, object]]
    """Custom metadata dictionary. Will be merged with existing metadata."""

    document_title: Optional[str]
    """Human-readable title for the contract"""

    filename: Optional[str]
    """Update the stored filename"""
