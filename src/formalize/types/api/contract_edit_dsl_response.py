# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ContractEditDslResponse"]


class ContractEditDslResponse(BaseModel):
    """Result of applying an edit (preview — not yet saved)."""

    change_description: str

    latency_seconds: float

    original_model_code: str

    success: bool

    updated_model_code: str

    changes_made: Optional[str] = None

    contract_clause: Optional[str] = None

    final_error: Optional[str] = None

    insertion_anchor_text: Optional[str] = None

    insertion_location: Optional[str] = None

    no_change_reason: Optional[str] = None
