# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .docx_change import DocxChange

__all__ = ["ContractEditFromTextResponse"]


class ContractEditFromTextResponse(BaseModel):
    """Result of applying inline text edits to the Catala formalization."""

    changes_applied: List[DocxChange]

    changes_skipped: List[DocxChange]

    latency_seconds: float

    original_catala: str

    success: bool

    updated_catala: str

    final_error: Optional[str] = None
