# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .docx_change import DocxChange

__all__ = ["ContractDiffDocxResponse"]


class ContractDiffDocxResponse(BaseModel):
    """Result of diffing the uploaded docx against the original."""

    changes: List[DocxChange]

    total_paragraphs_original: int

    total_paragraphs_uploaded: int
