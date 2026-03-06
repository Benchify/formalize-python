# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["FieldInfo"]


class FieldInfo(BaseModel):
    """Information about a single field (input, output, or internal) in a scope."""

    is_primitive: bool
    """
    True if the type is a primitive (integer, decimal, money, boolean, date,
    duration)
    """

    name: str
    """The field name as defined in the specification"""

    type_name: str
    """The type of the field (e.g., 'integer', 'money', 'PharmaClaim')"""
