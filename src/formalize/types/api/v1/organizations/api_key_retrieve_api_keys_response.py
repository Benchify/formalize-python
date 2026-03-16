# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from ....._models import BaseModel

__all__ = ["APIKeyRetrieveAPIKeysResponse", "APIKeyRetrieveAPIKeysResponseItem"]


class APIKeyRetrieveAPIKeysResponseItem(BaseModel):
    """API key information (without the actual key)."""

    created_at: datetime

    key_id: str

    name: str

    status: str


APIKeyRetrieveAPIKeysResponse: TypeAlias = List[APIKeyRetrieveAPIKeysResponseItem]
