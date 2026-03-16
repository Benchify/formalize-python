# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .org_member_info import OrgMemberInfo

__all__ = ["MemberListResponse"]

MemberListResponse: TypeAlias = List[OrgMemberInfo]
