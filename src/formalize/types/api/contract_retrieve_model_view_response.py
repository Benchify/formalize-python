# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ContractRetrieveModelViewResponse", "ScopeEdge", "VariableConnection"]


class ScopeEdge(BaseModel):
    """A directed dependency edge between two scopes."""

    source: str

    target: str

    source_output: Optional[str] = None


class VariableConnection(BaseModel):
    """A directed data-flow connection between two specific variables."""

    source_scope: str

    source_var: str

    target_scope: str

    target_var: str

    passthrough: Optional[bool] = None


class ContractRetrieveModelViewResponse(BaseModel):
    """Complete model view for a contract."""

    contract_id: str

    execution_order: List[str]

    filename: str

    scope_edges: List[ScopeEdge]

    sections: List["ModelSection"]

    variable_connections: List[VariableConnection]


from .model_section import ModelSection
