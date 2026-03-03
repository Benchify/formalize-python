# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DocxChange"]


class DocxChange(BaseModel):
    """A single detected difference between original and uploaded docx."""

    change_type: str

    paragraph_index: int

    new_text: Optional[str] = None

    old_text: Optional[str] = None
