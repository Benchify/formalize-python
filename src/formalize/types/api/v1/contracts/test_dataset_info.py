# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["TestDatasetInfo"]


class TestDatasetInfo(BaseModel):
    __test__ = False
    """Information about a single test dataset."""
    id: str
    """Unique dataset identifier"""

    contract_id: str
    """The contract this dataset belongs to"""

    created_at: datetime
    """When the dataset was uploaded"""

    file_type: str
    """File type: xlsx or csv"""

    filename: str
    """Original filename"""

    is_primary: bool
    """Whether this is the primary/default dataset"""

    name: str
    """User-friendly name for the dataset"""

    updated_at: datetime
    """When the dataset was last modified"""

    column_names: Optional[List[str]] = None
    """Column names in the dataset"""

    description: Optional[str] = None
    """Description of what this dataset tests"""

    row_count: Optional[int] = None
    """Number of data rows"""
