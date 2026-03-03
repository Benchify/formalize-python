# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from ..v1.formalization_status import FormalizationStatus

__all__ = ["FormalizeCreateResponse"]


class FormalizeCreateResponse(BaseModel):
    """202 Accepted response: formalization task has been started in the background.

    Clients should poll GET /contracts/{contract_id} to check formalization_status.
    """

    contract_id: str

    formalization_status: FormalizationStatus
