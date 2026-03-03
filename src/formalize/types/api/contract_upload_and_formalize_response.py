# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .contract_document import ContractDocument

__all__ = ["ContractUploadAndFormalizeResponse"]


class ContractUploadAndFormalizeResponse(BaseModel):
    """202 Accepted response: document uploaded and formalization task started.

    Clients should poll GET /contracts/{contract_id} to check formalization_status.
    """

    contract: ContractDocument
