# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .....types.api.v1.contracts import spec_create_params
from .....types.api.v1.contracts.spec_list_response import SpecListResponse
from .....types.api.v1.contracts.spec_create_response import SpecCreateResponse

__all__ = ["SpecResource", "AsyncSpecResource"]


class SpecResource(SyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> SpecResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return SpecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpecResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return SpecResourceWithStreamingResponse(self)

    def create(
        self,
        contract_id: str,
        *,
        model_code: str,
        validate_syntax: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpecCreateResponse:
        """
        Update the formal specification for a contract.

        Args:
          model_code: The complete specification source code for the contract. This should be valid
              specification code.

          validate_syntax: If true, validate the specification syntax before saving. Set to false to save
              draft code that may have errors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._put(
            f"/api/v1/contracts/{contract_id}/spec",
            body=maybe_transform(
                {
                    "model_code": model_code,
                    "validate_syntax": validate_syntax,
                },
                spec_create_params.SpecCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpecCreateResponse,
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
    ) -> SpecListResponse:
        """
        Get the formal specification for a contract.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/v1/contracts/{contract_id}/spec",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpecListResponse,
        )


class AsyncSpecResource(AsyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> AsyncSpecResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpecResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return AsyncSpecResourceWithStreamingResponse(self)

    async def create(
        self,
        contract_id: str,
        *,
        model_code: str,
        validate_syntax: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpecCreateResponse:
        """
        Update the formal specification for a contract.

        Args:
          model_code: The complete specification source code for the contract. This should be valid
              specification code.

          validate_syntax: If true, validate the specification syntax before saving. Set to false to save
              draft code that may have errors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._put(
            f"/api/v1/contracts/{contract_id}/spec",
            body=await async_maybe_transform(
                {
                    "model_code": model_code,
                    "validate_syntax": validate_syntax,
                },
                spec_create_params.SpecCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpecCreateResponse,
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
    ) -> SpecListResponse:
        """
        Get the formal specification for a contract.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/v1/contracts/{contract_id}/spec",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpecListResponse,
        )


class SpecResourceWithRawResponse:
    def __init__(self, spec: SpecResource) -> None:
        self._spec = spec

        self.create = to_raw_response_wrapper(
            spec.create,
        )
        self.list = to_raw_response_wrapper(
            spec.list,
        )


class AsyncSpecResourceWithRawResponse:
    def __init__(self, spec: AsyncSpecResource) -> None:
        self._spec = spec

        self.create = async_to_raw_response_wrapper(
            spec.create,
        )
        self.list = async_to_raw_response_wrapper(
            spec.list,
        )


class SpecResourceWithStreamingResponse:
    def __init__(self, spec: SpecResource) -> None:
        self._spec = spec

        self.create = to_streamed_response_wrapper(
            spec.create,
        )
        self.list = to_streamed_response_wrapper(
            spec.list,
        )


class AsyncSpecResourceWithStreamingResponse:
    def __init__(self, spec: AsyncSpecResource) -> None:
        self._spec = spec

        self.create = async_to_streamed_response_wrapper(
            spec.create,
        )
        self.list = async_to_streamed_response_wrapper(
            spec.list,
        )
