# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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

__all__ = ["OptimizationResultsResource", "AsyncOptimizationResultsResource"]


class OptimizationResultsResource(SyncAPIResource):
    """Contract optimization and AI-powered redline generation"""

    @cached_property
    def with_raw_response(self) -> OptimizationResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#accessing-raw-response-data-eg-headers
        """
        return OptimizationResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptimizationResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#with_streaming_response
        """
        return OptimizationResultsResourceWithStreamingResponse(self)

    def delete_optimization_results(
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
        Delete AI-generated redlines and clear optimization results.

        This clears:

        - All AI-generated redlines
        - Contract optimization_results
        - optimization_context and explanation from opposing redlines (so they get
          re-analyzed)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._delete(
            f"/api/contracts/{contract_id}/optimization-results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_optimization_results(
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
        Get Optimization Results

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/optimization-results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOptimizationResultsResource(AsyncAPIResource):
    """Contract optimization and AI-powered redline generation"""

    @cached_property
    def with_raw_response(self) -> AsyncOptimizationResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptimizationResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptimizationResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#with_streaming_response
        """
        return AsyncOptimizationResultsResourceWithStreamingResponse(self)

    async def delete_optimization_results(
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
        Delete AI-generated redlines and clear optimization results.

        This clears:

        - All AI-generated redlines
        - Contract optimization_results
        - optimization_context and explanation from opposing redlines (so they get
          re-analyzed)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._delete(
            f"/api/contracts/{contract_id}/optimization-results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_optimization_results(
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
        Get Optimization Results

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/optimization-results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OptimizationResultsResourceWithRawResponse:
    def __init__(self, optimization_results: OptimizationResultsResource) -> None:
        self._optimization_results = optimization_results

        self.delete_optimization_results = to_raw_response_wrapper(
            optimization_results.delete_optimization_results,
        )
        self.retrieve_optimization_results = to_raw_response_wrapper(
            optimization_results.retrieve_optimization_results,
        )


class AsyncOptimizationResultsResourceWithRawResponse:
    def __init__(self, optimization_results: AsyncOptimizationResultsResource) -> None:
        self._optimization_results = optimization_results

        self.delete_optimization_results = async_to_raw_response_wrapper(
            optimization_results.delete_optimization_results,
        )
        self.retrieve_optimization_results = async_to_raw_response_wrapper(
            optimization_results.retrieve_optimization_results,
        )


class OptimizationResultsResourceWithStreamingResponse:
    def __init__(self, optimization_results: OptimizationResultsResource) -> None:
        self._optimization_results = optimization_results

        self.delete_optimization_results = to_streamed_response_wrapper(
            optimization_results.delete_optimization_results,
        )
        self.retrieve_optimization_results = to_streamed_response_wrapper(
            optimization_results.retrieve_optimization_results,
        )


class AsyncOptimizationResultsResourceWithStreamingResponse:
    def __init__(self, optimization_results: AsyncOptimizationResultsResource) -> None:
        self._optimization_results = optimization_results

        self.delete_optimization_results = async_to_streamed_response_wrapper(
            optimization_results.delete_optimization_results,
        )
        self.retrieve_optimization_results = async_to_streamed_response_wrapper(
            optimization_results.retrieve_optimization_results,
        )
