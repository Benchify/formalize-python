# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ContractGetDependenciesResponse", "ScopeEdge", "VariableConnection"]


class ScopeEdge(BaseModel):
    """A directed dependency edge between two scopes."""

    source: str
    """Source scope name"""

    target: str
    """Target scope name (depends on source)"""

    source_output: Optional[str] = None
    """Specific output variable from source, if known"""


class VariableConnection(BaseModel):
    """A directed data-flow connection between two variables."""

    source_scope: str
    """Scope containing the source variable"""

    source_var: str
    """Variable name in source scope"""

    target_scope: str
    """Scope containing the target variable"""

    target_var: str
    """Variable name in target scope"""

    is_passthrough: Optional[bool] = None
    """True if source_var is an input passed through to a sub-scope"""


class ContractGetDependenciesResponse(BaseModel):
    """Variable and scope dependencies for a contract."""

    contract_id: str
    """The contract's ID"""

    execution_order: List[str]
    """Scopes in topological execution order"""

    scope_edges: List[ScopeEdge]
    """Directed edges between scopes"""

    variable_connections: List[VariableConnection]
    """Data-flow connections between variables"""
