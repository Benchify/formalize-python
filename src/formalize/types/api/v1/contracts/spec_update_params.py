# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SpecUpdateParams"]


class SpecUpdateParams(TypedDict, total=False):
    catala_code: Required[str]
    """The complete Catala source code for the contract.

    This should be valid Catala code that compiles without errors.
    """

    validate_syntax: bool
    """If true, validate the Catala code syntax before saving.

    Set to false to save draft code that may have errors.
    """
