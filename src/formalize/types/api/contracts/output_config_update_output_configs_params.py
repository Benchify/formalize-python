# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["OutputConfigUpdateOutputConfigsParams", "OutputConfig"]


class OutputConfigUpdateOutputConfigsParams(TypedDict, total=False):
    output_configs: Required[Iterable[OutputConfig]]


class OutputConfig(TypedDict, total=False):
    """Request model for updating a single output configuration."""

    name: Required[str]
    """The output variable name"""

    direction: Optional[str]
    """Desired direction: 'increase' or 'decrease'"""

    display_name: Optional[str]
    """Human-readable display name"""

    enabled: Optional[bool]
    """Whether to show this output in the data view"""
