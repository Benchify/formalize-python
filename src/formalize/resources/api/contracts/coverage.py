# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.contracts import coverage_create_params

__all__ = ["CoverageResource", "AsyncCoverageResource"]


class CoverageResource(SyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> CoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#accessing-raw-response-data-eg-headers
        """
        return CoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#with_streaming_response
        """
        return CoverageResourceWithStreamingResponse(self)

    def create(
        self,
        contract_id: str,
        *,
        regenerate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Generate formalization coverage for a contract.

        This uses an LLM to analyze the contract paragraphs and Catala code, creating
        attributions that link document text to formalized expressions.

        Args: contract_id: ID of the contract regenerate: If True, regenerate even if
        coverage already exists

        Returns: The complete coverage with all attributions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/coverage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"regenerate": regenerate}, coverage_create_params.CoverageCreateParams),
            ),
            cast_to=object,
        )

    def list(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get the formalization coverage for a contract.

        Returns the complete coverage with all paragraph attributions and expressions.
        Returns 404 if no coverage exists or if it's not completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/coverage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_status(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get the status of formalization coverage for a contract.

        Returns whether coverage exists, its status, and basic metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/coverage/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncCoverageResource(AsyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> AsyncCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#with_streaming_response
        """
        return AsyncCoverageResourceWithStreamingResponse(self)

    async def create(
        self,
        contract_id: str,
        *,
        regenerate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Generate formalization coverage for a contract.

        This uses an LLM to analyze the contract paragraphs and Catala code, creating
        attributions that link document text to formalized expressions.

        Args: contract_id: ID of the contract regenerate: If True, regenerate even if
        coverage already exists

        Returns: The complete coverage with all attributions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/coverage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"regenerate": regenerate}, coverage_create_params.CoverageCreateParams
                ),
            ),
            cast_to=object,
        )

    async def list(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get the formalization coverage for a contract.

        Returns the complete coverage with all paragraph attributions and expressions.
        Returns 404 if no coverage exists or if it's not completed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/coverage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_status(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get the status of formalization coverage for a contract.

        Returns whether coverage exists, its status, and basic metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/coverage/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class CoverageResourceWithRawResponse:
    def __init__(self, coverage: CoverageResource) -> None:
        self._coverage = coverage

        self.create = to_raw_response_wrapper(
            coverage.create,
        )
        self.list = to_raw_response_wrapper(
            coverage.list,
        )
        self.retrieve_status = to_raw_response_wrapper(
            coverage.retrieve_status,
        )


class AsyncCoverageResourceWithRawResponse:
    def __init__(self, coverage: AsyncCoverageResource) -> None:
        self._coverage = coverage

        self.create = async_to_raw_response_wrapper(
            coverage.create,
        )
        self.list = async_to_raw_response_wrapper(
            coverage.list,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            coverage.retrieve_status,
        )


class CoverageResourceWithStreamingResponse:
    def __init__(self, coverage: CoverageResource) -> None:
        self._coverage = coverage

        self.create = to_streamed_response_wrapper(
            coverage.create,
        )
        self.list = to_streamed_response_wrapper(
            coverage.list,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            coverage.retrieve_status,
        )


class AsyncCoverageResourceWithStreamingResponse:
    def __init__(self, coverage: AsyncCoverageResource) -> None:
        self._coverage = coverage

        self.create = async_to_streamed_response_wrapper(
            coverage.create,
        )
        self.list = async_to_streamed_response_wrapper(
            coverage.list,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            coverage.retrieve_status,
        )
