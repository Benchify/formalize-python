# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .organization_info import OrganizationInfo

__all__ = ["MeRetrieveOrganizationsResponse"]

MeRetrieveOrganizationsResponse: TypeAlias = List[OrganizationInfo]
