# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ....._models import BaseModel

__all__ = ["AuditRunResponse"]


class AuditRunResponse(BaseModel):
    """Response from auditing a contract computation."""

    contract_id: str
    """The contract that was audited"""

    inputs_provided: Dict[str, object]
    """The inputs that were provided"""

    outputs: Dict[str, object]
    """The computed output values from the main scope"""

    scope_executed: str
    """The scope that was executed"""

    success: bool
    """Whether the computation succeeded"""

    all_scopes: Optional[Dict[str, Dict[str, object]]] = None
    """All variable values organized by scope (for detailed audit trail)"""

    error: Optional[str] = None
    """Error message if computation failed"""

    execution_time_ms: Optional[int] = None
    """Execution time in milliseconds"""
