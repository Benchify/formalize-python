# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .redline_status import RedlineStatus

__all__ = ["RedlineUpdateParams"]


class RedlineUpdateParams(TypedDict, total=False):
    contract_id: Required[str]

    comment_text: Optional[str]

    new_text: Optional[str]

    old_text: Optional[str]

    status: Optional[RedlineStatus]
