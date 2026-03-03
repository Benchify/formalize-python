# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["DocxUpdateResponse"]


class DocxUpdateResponse(BaseModel):
    """Response after updating the DOCX document."""

    contract_id: str
    """The updated contract's ID"""

    file_size_bytes: int
    """Size of the uploaded file in bytes"""

    filename: str
    """The stored filename"""

    success: bool
    """Whether the upload succeeded"""

    updated_at: datetime
    """Timestamp of the update"""

    document_title: Optional[str] = None
    """The document title"""
