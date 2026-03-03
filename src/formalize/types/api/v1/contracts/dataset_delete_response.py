# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["DatasetDeleteResponse"]


class DatasetDeleteResponse(BaseModel):
    """Response after deleting a test dataset."""

    dataset_id: str
    """The deleted dataset's ID"""

    message: str
    """Confirmation message"""

    success: bool
    """Whether the deletion succeeded"""
