# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .contract_document_response import ContractDocumentResponse

__all__ = ["ContractRetrieveResponse"]


class ContractRetrieveResponse(BaseModel):
    contracts: List[ContractDocumentResponse]

    total: int
