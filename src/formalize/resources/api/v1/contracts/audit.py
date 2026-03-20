# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.contracts import audit_batch_params, audit_create_params
from .....types.api.v1.contracts.audit_batch_response import AuditBatchResponse
from .....types.api.v1.contracts.audit_create_response import AuditCreateResponse

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

    def create(
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
    ) -> AuditCreateResponse:
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
            path_template("/api/v1/contracts/{contract_id}/audit", contract_id=contract_id),
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "scope_name": scope_name,
                },
                audit_create_params.AuditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditCreateResponse,
        )

    def batch(
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
    ) -> AuditBatchResponse:
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
            path_template("/api/v1/contracts/{contract_id}/audit/batch", contract_id=contract_id),
            body=maybe_transform(
                {
                    "scenarios": scenarios,
                    "scope_name": scope_name,
                },
                audit_batch_params.AuditBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditBatchResponse,
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

    async def create(
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
    ) -> AuditCreateResponse:
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
            path_template("/api/v1/contracts/{contract_id}/audit", contract_id=contract_id),
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "scope_name": scope_name,
                },
                audit_create_params.AuditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditCreateResponse,
        )

    async def batch(
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
    ) -> AuditBatchResponse:
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
            path_template("/api/v1/contracts/{contract_id}/audit/batch", contract_id=contract_id),
            body=await async_maybe_transform(
                {
                    "scenarios": scenarios,
                    "scope_name": scope_name,
                },
                audit_batch_params.AuditBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditBatchResponse,
        )


class AuditResourceWithRawResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.create = to_raw_response_wrapper(
            audit.create,
        )
        self.batch = to_raw_response_wrapper(
            audit.batch,
        )


class AsyncAuditResourceWithRawResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.create = async_to_raw_response_wrapper(
            audit.create,
        )
        self.batch = async_to_raw_response_wrapper(
            audit.batch,
        )


class AuditResourceWithStreamingResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.create = to_streamed_response_wrapper(
            audit.create,
        )
        self.batch = to_streamed_response_wrapper(
            audit.batch,
        )


class AsyncAuditResourceWithStreamingResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.create = async_to_streamed_response_wrapper(
            audit.create,
        )
        self.batch = async_to_streamed_response_wrapper(
            audit.batch,
        )
