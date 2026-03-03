# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .contract_document import ContractDocument

__all__ = ["ContractListResponse"]


class ContractListResponse(BaseModel):
    contracts: List[ContractDocument]

    total: int
