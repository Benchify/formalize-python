# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel
from .test_dataset_info import TestDatasetInfo

__all__ = ["DatasetUploadResponse"]


class DatasetUploadResponse(BaseModel):
    """Response after creating a test dataset."""

    dataset: TestDatasetInfo
    """The created dataset"""

    success: bool
    """Whether the upload succeeded"""
