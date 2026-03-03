# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .change_type import ChangeType
from .redline_status import RedlineStatus

__all__ = ["RedlineResponse"]


class RedlineResponse(BaseModel):
    id: str

    change_type: ChangeType

    comment_text: Optional[str] = None

    contract_id: str

    contributor_name: str

    created_at: datetime

    end_offset: int

    explanation: Optional[str] = None

    new_text: Optional[str] = None

    old_text: Optional[str] = None

    paragraph_index: int

    redline_type: Literal["ORIGINAL", "AI_GENERATED", "USER_EDITED", "HUMAN_AUTHORED"]

    start_offset: int

    status: RedlineStatus

    updated_at: datetime

    insertion_anchor_text: Optional[str] = None

    justification: Optional[Dict[str, object]] = None

    optimization_context: Optional[Dict[str, object]] = None
