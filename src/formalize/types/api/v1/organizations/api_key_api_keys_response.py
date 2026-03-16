# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ....._models import BaseModel

__all__ = ["APIKeyAPIKeysResponse"]


class APIKeyAPIKeysResponse(BaseModel):
    """Response after creating an API key."""

    api_key: str

    created_at: datetime

    key_id: str

    name: str
