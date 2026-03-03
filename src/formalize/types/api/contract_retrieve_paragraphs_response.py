# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ContractRetrieveParagraphsResponse"]


class ContractRetrieveParagraphsResponse(BaseModel):
    """Paragraphs extracted from the original docx for in-browser editing."""

    paragraphs: List[str]
