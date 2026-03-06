# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContractCreateParams"]


class ContractCreateParams(TypedDict, total=False):
    docx_base64: Required[str]
    """Base64-encoded content of the DOCX file"""

    filename: Required[str]
    """Original filename of the DOCX document"""

    document_title: Optional[str]
    """Human-readable title. If not provided, will be extracted from DOCX."""

    model_code: Optional[str]
    """Optional pre-existing formalization code"""

    org_id: Optional[str]
    """Organization ID to associate with this contract"""
