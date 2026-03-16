# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["OrgMemberInfo"]


class OrgMemberInfo(BaseModel):
    """Organization member information."""

    email: str

    joined_at: datetime

    member_id: str

    role: str

    user_id: str

    display_name: Optional[str] = None
