# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .test_dataset_info import TestDatasetInfo

__all__ = ["DatasetListResponse"]


class DatasetListResponse(BaseModel):
    """Response containing all test datasets for a contract."""

    contract_id: str
    """The contract's ID"""

    datasets: List[TestDatasetInfo]
    """List of datasets"""

    total: int
    """Total number of datasets"""

    primary_dataset_id: Optional[str] = None
    """ID of the primary dataset, if one is set"""
