# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.contracts import audit_run_params, audit_run_batch_params
from .....types.api.v1.contracts.audit_run_response import AuditRunResponse
from .....types.api.v1.contracts.audit_run_batch_response import AuditRunBatchResponse

__all__ = ["AuditResource", "AsyncAuditResource"]


class AuditResource(SyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> AuditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AuditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return AuditResourceWithStreamingResponse(self)

    def run(
        self,
        contract_id: str,
        *,
        inputs: Dict[str, object],
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditRunResponse:
        """
        Execute a contract computation with given inputs and return the results.

        Args:
          inputs: Input values for the computation. Keys are field names, values match the
              expected types.

          scope_name: The scope to execute. If not provided, uses the contract's main scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/v1/contracts/{contract_id}/audit",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "scope_name": scope_name,
                },
                audit_run_params.AuditRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditRunResponse,
        )

    def run_batch(
        self,
        contract_id: str,
        *,
        scenarios: Iterable[Dict[str, object]],
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditRunBatchResponse:
        """
        Execute a contract computation with multiple input scenarios.

        Args:
          scenarios: List of input scenarios to evaluate

          scope_name: The scope to execute. If not provided, uses the contract's main scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/v1/contracts/{contract_id}/audit/batch",
            body=maybe_transform(
                {
                    "scenarios": scenarios,
                    "scope_name": scope_name,
                },
                audit_run_batch_params.AuditRunBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditRunBatchResponse,
        )


class AsyncAuditResource(AsyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> AsyncAuditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return AsyncAuditResourceWithStreamingResponse(self)

    async def run(
        self,
        contract_id: str,
        *,
        inputs: Dict[str, object],
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditRunResponse:
        """
        Execute a contract computation with given inputs and return the results.

        Args:
          inputs: Input values for the computation. Keys are field names, values match the
              expected types.

          scope_name: The scope to execute. If not provided, uses the contract's main scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/v1/contracts/{contract_id}/audit",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "scope_name": scope_name,
                },
                audit_run_params.AuditRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditRunResponse,
        )

    async def run_batch(
        self,
        contract_id: str,
        *,
        scenarios: Iterable[Dict[str, object]],
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditRunBatchResponse:
        """
        Execute a contract computation with multiple input scenarios.

        Args:
          scenarios: List of input scenarios to evaluate

          scope_name: The scope to execute. If not provided, uses the contract's main scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/v1/contracts/{contract_id}/audit/batch",
            body=await async_maybe_transform(
                {
                    "scenarios": scenarios,
                    "scope_name": scope_name,
                },
                audit_run_batch_params.AuditRunBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditRunBatchResponse,
        )


class AuditResourceWithRawResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.run = to_raw_response_wrapper(
            audit.run,
        )
        self.run_batch = to_raw_response_wrapper(
            audit.run_batch,
        )


class AsyncAuditResourceWithRawResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.run = async_to_raw_response_wrapper(
            audit.run,
        )
        self.run_batch = async_to_raw_response_wrapper(
            audit.run_batch,
        )


class AuditResourceWithStreamingResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.run = to_streamed_response_wrapper(
            audit.run,
        )
        self.run_batch = to_streamed_response_wrapper(
            audit.run_batch,
        )


class AsyncAuditResourceWithStreamingResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.run = async_to_streamed_response_wrapper(
            audit.run,
        )
        self.run_batch = async_to_streamed_response_wrapper(
            audit.run_batch,
        )
