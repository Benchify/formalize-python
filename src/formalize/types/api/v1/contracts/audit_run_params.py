# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AuditRunParams"]


class AuditRunParams(TypedDict, total=False):
    inputs: Required[Dict[str, object]]
    """Input values for the computation.

    Keys are field names, values match the expected types.
    """

    scope_name: Optional[str]
    """The scope to execute. If not provided, uses the contract's main scope."""
