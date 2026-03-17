# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ....types.api import contract_optimize_params
from ...._base_client import make_request_options
from .optimization_results import (
    OptimizationResultsResource,
    AsyncOptimizationResultsResource,
    OptimizationResultsResourceWithRawResponse,
    AsyncOptimizationResultsResourceWithRawResponse,
    OptimizationResultsResourceWithStreamingResponse,
    AsyncOptimizationResultsResourceWithStreamingResponse,
)

__all__ = ["ContractsResource", "AsyncContractsResource"]


class ContractsResource(SyncAPIResource):
    """Contract optimization and AI-powered redline generation"""

    @cached_property
    def optimization_results(self) -> OptimizationResultsResource:
        """Contract optimization and AI-powered redline generation"""
        return OptimizationResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return ContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return ContractsResourceWithStreamingResponse(self)

    def optimize(
        self,
        contract_id: str,
        *,
        analysis_concurrency: int | Omit = omit,
        num_test_inputs: int | Omit = omit,
        output_var: Optional[str] | Omit = omit,
        party_position: str | Omit = omit,
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Run Optimization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/optimize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "analysis_concurrency": analysis_concurrency,
                        "num_test_inputs": num_test_inputs,
                        "output_var": output_var,
                        "party_position": party_position,
                        "scope_name": scope_name,
                    },
                    contract_optimize_params.ContractOptimizeParams,
                ),
            ),
            cast_to=object,
        )


class AsyncContractsResource(AsyncAPIResource):
    """Contract optimization and AI-powered redline generation"""

    @cached_property
    def optimization_results(self) -> AsyncOptimizationResultsResource:
        """Contract optimization and AI-powered redline generation"""
        return AsyncOptimizationResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return AsyncContractsResourceWithStreamingResponse(self)

    async def optimize(
        self,
        contract_id: str,
        *,
        analysis_concurrency: int | Omit = omit,
        num_test_inputs: int | Omit = omit,
        output_var: Optional[str] | Omit = omit,
        party_position: str | Omit = omit,
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Run Optimization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/optimize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "analysis_concurrency": analysis_concurrency,
                        "num_test_inputs": num_test_inputs,
                        "output_var": output_var,
                        "party_position": party_position,
                        "scope_name": scope_name,
                    },
                    contract_optimize_params.ContractOptimizeParams,
                ),
            ),
            cast_to=object,
        )


class ContractsResourceWithRawResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.optimize = to_raw_response_wrapper(
            contracts.optimize,
        )

    @cached_property
    def optimization_results(self) -> OptimizationResultsResourceWithRawResponse:
        """Contract optimization and AI-powered redline generation"""
        return OptimizationResultsResourceWithRawResponse(self._contracts.optimization_results)


class AsyncContractsResourceWithRawResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.optimize = async_to_raw_response_wrapper(
            contracts.optimize,
        )

    @cached_property
    def optimization_results(self) -> AsyncOptimizationResultsResourceWithRawResponse:
        """Contract optimization and AI-powered redline generation"""
        return AsyncOptimizationResultsResourceWithRawResponse(self._contracts.optimization_results)


class ContractsResourceWithStreamingResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.optimize = to_streamed_response_wrapper(
            contracts.optimize,
        )

    @cached_property
    def optimization_results(self) -> OptimizationResultsResourceWithStreamingResponse:
        """Contract optimization and AI-powered redline generation"""
        return OptimizationResultsResourceWithStreamingResponse(self._contracts.optimization_results)


class AsyncContractsResourceWithStreamingResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.optimize = async_to_streamed_response_wrapper(
            contracts.optimize,
        )

    @cached_property
    def optimization_results(self) -> AsyncOptimizationResultsResourceWithStreamingResponse:
        """Contract optimization and AI-powered redline generation"""
        return AsyncOptimizationResultsResourceWithStreamingResponse(self._contracts.optimization_results)
