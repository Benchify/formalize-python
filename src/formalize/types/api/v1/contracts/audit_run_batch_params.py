# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AuditRunBatchParams"]


class AuditRunBatchParams(TypedDict, total=False):
    scenarios: Required[Iterable[Dict[str, object]]]
    """List of input scenarios to evaluate"""

    scope_name: Optional[str]
    """The scope to execute. If not provided, uses the contract's main scope."""
