# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ....._models import BaseModel

__all__ = ["AuditBatchResponse", "Result"]


class Result(BaseModel):
    """Result for a single scenario in a batch audit."""

    scenario_index: int
    """Index of this scenario in the request"""

    success: bool
    """Whether this scenario succeeded"""

    error: Optional[str] = None
    """Error message if this scenario failed"""

    outputs: Optional[Dict[str, object]] = None
    """The computed output values"""


class AuditBatchResponse(BaseModel):
    """Response from batch auditing multiple scenarios."""

    contract_id: str
    """The contract that was audited"""

    execution_time_ms: int
    """Total execution time in milliseconds"""

    failed: int
    """Number of scenarios that failed"""

    results: List[Result]
    """Results for each scenario"""

    scope_executed: str
    """The scope that was executed"""

    successful: int
    """Number of scenarios that succeeded"""

    total_scenarios: int
    """Total number of scenarios submitted"""
