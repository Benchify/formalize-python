# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SpecUpdateParams"]


class SpecUpdateParams(TypedDict, total=False):
    model_code: Required[str]
    """The complete specification source code for the contract.

    This should be valid specification code.
    """

    validate_syntax: bool
    """If true, validate the specification syntax before saving.

    Set to false to save draft code that may have errors.
    """
