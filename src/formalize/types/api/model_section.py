# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["ModelSection", "Declaration", "Scope"]


class Declaration(BaseModel):
    """A struct or enum declaration extracted from a specification section."""

    kind: str

    line_start: int

    name: str

    fields: Optional[List[List[object]]] = None

    variants: Optional[List[str]] = None


class Scope(BaseModel):
    """A scope's interface (inputs/outputs/internals)."""

    inputs: List[Dict[str, str]]

    internals: List[Dict[str, str]]

    line_start: int

    name: str

    outputs: List[Dict[str, str]]

    definitions: Optional[Dict[str, str]] = None


class ModelSection(BaseModel):
    """A section of the contract with its formal specification content."""

    children: List["ModelSection"]

    declarations: List[Declaration]

    english_text: str

    scopes: List[Scope]

    title: str

    paragraph_index: Optional[int] = None
