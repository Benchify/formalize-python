# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DocxCreateParams"]


class DocxCreateParams(TypedDict, total=False):
    docx_base64: Required[str]
    """Base64-encoded content of the DOCX file"""

    document_title: Optional[str]
    """Human-readable title for the document.

    If not provided, keeps existing or extracts from DOCX.
    """

    filename: Optional[str]
    """New filename for the document. If not provided, keeps the existing filename."""
