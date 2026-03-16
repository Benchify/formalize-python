# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["OrganizationInfo"]


class OrganizationInfo(BaseModel):
    """Organization information."""

    created_at: datetime

    org_id: str

    org_type: str

    member_count: Optional[int] = None

    org_name: Optional[str] = None

    slug: Optional[str] = None

    user_role: Optional[str] = None
