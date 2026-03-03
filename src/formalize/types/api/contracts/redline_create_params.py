# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .change_type import ChangeType
from .redline_status import RedlineStatus

__all__ = ["RedlineCreateParams"]


class RedlineCreateParams(TypedDict, total=False):
    change_type: Required[ChangeType]

    contributor_name: str

    explanation: Optional[str]

    insertion_anchor_text: Optional[str]

    new_text: Optional[str]

    old_text: Optional[str]

    optimization_context: Optional[Dict[str, object]]

    paragraph_index: int

    status: RedlineStatus
