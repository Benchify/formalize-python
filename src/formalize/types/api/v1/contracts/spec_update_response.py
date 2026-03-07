# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["SpecUpdateResponse"]


class SpecUpdateResponse(BaseModel):
    """Response after updating the formal specification."""

    contract_id: str
    """The updated contract's ID"""

    enum_count: int
    """Number of enum types in the updated code"""

    scope_count: int
    """Number of scopes in the updated code"""

    struct_count: int
    """Number of struct types in the updated code"""

    success: bool
    """Whether the update succeeded"""

    updated_at: datetime
    """Timestamp of the update"""

    validation_passed: bool
    """Whether the specification passed syntax validation"""

    validation_errors: Optional[List[str]] = None
    """List of validation errors if validation failed"""
