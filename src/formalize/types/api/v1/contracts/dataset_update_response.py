# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel
from .test_dataset_info import TestDatasetInfo

__all__ = ["DatasetUpdateResponse"]


class DatasetUpdateResponse(BaseModel):
    """Response after updating a test dataset."""

    dataset: TestDatasetInfo
    """The updated dataset"""

    success: bool
    """Whether the update succeeded"""
