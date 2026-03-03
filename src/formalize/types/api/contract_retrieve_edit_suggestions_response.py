# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ContractRetrieveEditSuggestionsResponse", "Suggestion"]


class Suggestion(BaseModel):
    """A single edit suggestion for a contract."""

    label: str

    rationale: str


class ContractRetrieveEditSuggestionsResponse(BaseModel):
    """Response containing AI-generated edit suggestions."""

    suggestions: List[Suggestion]

    generated_at: Optional[datetime] = None

    optimization_direction: Optional[str] = None

    output_variable: Optional[str] = None
