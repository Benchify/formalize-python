# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["DocxListResponse"]


class DocxListResponse(BaseModel):
    """Response containing the DOCX document metadata and download info."""

    contract_id: str
    """The contract's ID"""

    download_url: str
    """URL to download the DOCX file (use GET request with same auth)"""

    filename: str
    """The original filename"""

    has_docx: bool
    """Whether the contract has a DOCX file stored"""

    document_title: Optional[str] = None
    """The document title"""

    file_size_bytes: Optional[int] = None
    """Size of the file in bytes, if available"""
