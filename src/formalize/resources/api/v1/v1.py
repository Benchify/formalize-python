# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .me import (
    MeResource,
    AsyncMeResource,
    MeResourceWithRawResponse,
    AsyncMeResourceWithRawResponse,
    MeResourceWithStreamingResponse,
    AsyncMeResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .contracts.contracts import (
    ContractsResource,
    AsyncContractsResource,
    ContractsResourceWithRawResponse,
    AsyncContractsResourceWithRawResponse,
    ContractsResourceWithStreamingResponse,
    AsyncContractsResourceWithStreamingResponse,
)
from .organizations.organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def contracts(self) -> ContractsResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return ContractsResource(self._client)

    @cached_property
    def me(self) -> MeResource:
        """User profile management - create, read, update user accounts"""
        return MeResource(self._client)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        """User profile management - create, read, update user accounts"""
        return OrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def health_check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Check if the API server is running and healthy (v1 endpoint)."""
        return self._get(
            "/api/v1/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def contracts(self) -> AsyncContractsResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncContractsResource(self._client)

    @cached_property
    def me(self) -> AsyncMeResource:
        """User profile management - create, read, update user accounts"""
        return AsyncMeResource(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        """User profile management - create, read, update user accounts"""
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def health_check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Check if the API server is running and healthy (v1 endpoint)."""
        return await self._get(
            "/api/v1/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.health_check = to_raw_response_wrapper(
            v1.health_check,
        )

    @cached_property
    def contracts(self) -> ContractsResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return ContractsResourceWithRawResponse(self._v1.contracts)

    @cached_property
    def me(self) -> MeResourceWithRawResponse:
        """User profile management - create, read, update user accounts"""
        return MeResourceWithRawResponse(self._v1.me)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        """User profile management - create, read, update user accounts"""
        return OrganizationsResourceWithRawResponse(self._v1.organizations)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.health_check = async_to_raw_response_wrapper(
            v1.health_check,
        )

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncContractsResourceWithRawResponse(self._v1.contracts)

    @cached_property
    def me(self) -> AsyncMeResourceWithRawResponse:
        """User profile management - create, read, update user accounts"""
        return AsyncMeResourceWithRawResponse(self._v1.me)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        """User profile management - create, read, update user accounts"""
        return AsyncOrganizationsResourceWithRawResponse(self._v1.organizations)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.health_check = to_streamed_response_wrapper(
            v1.health_check,
        )

    @cached_property
    def contracts(self) -> ContractsResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return ContractsResourceWithStreamingResponse(self._v1.contracts)

    @cached_property
    def me(self) -> MeResourceWithStreamingResponse:
        """User profile management - create, read, update user accounts"""
        return MeResourceWithStreamingResponse(self._v1.me)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        """User profile management - create, read, update user accounts"""
        return OrganizationsResourceWithStreamingResponse(self._v1.organizations)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.health_check = async_to_streamed_response_wrapper(
            v1.health_check,
        )

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncContractsResourceWithStreamingResponse(self._v1.contracts)

    @cached_property
    def me(self) -> AsyncMeResourceWithStreamingResponse:
        """User profile management - create, read, update user accounts"""
        return AsyncMeResourceWithStreamingResponse(self._v1.me)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """User profile management - create, read, update user accounts"""
        return AsyncOrganizationsResourceWithStreamingResponse(self._v1.organizations)
