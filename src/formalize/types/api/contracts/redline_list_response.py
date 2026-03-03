# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .redline_response import RedlineResponse

__all__ = ["RedlineListResponse"]


class RedlineListResponse(BaseModel):
    redlines: List[RedlineResponse]

    total: int
