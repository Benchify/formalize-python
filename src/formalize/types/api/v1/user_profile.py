# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["UserProfile"]


class UserProfile(BaseModel):
    """User profile information."""

    created_at: datetime

    email: str

    user_id: str

    display_name: Optional[str] = None

    linkedin_url: Optional[str] = None

    photo_url: Optional[str] = None
