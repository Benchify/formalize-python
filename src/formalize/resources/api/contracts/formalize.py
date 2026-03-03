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
from ...._base_client import make_request_options
from ....types.api.contracts import formalize_create_params
from ....types.api.contracts.formalize_create_response import FormalizeCreateResponse

__all__ = ["FormalizeResource", "AsyncFormalizeResource"]


class FormalizeResource(SyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> FormalizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#accessing-raw-response-data-eg-headers
        """
        return FormalizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FormalizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#with_streaming_response
        """
        return FormalizeResourceWithStreamingResponse(self)

    def create(
        self,
        contract_id: str,
        *,
        max_prompts: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormalizeCreateResponse:
        """
        Start background formalization of a contract document into Catala code.

        Returns 202 Accepted immediately. Poll GET /{contract_id} for
        formalization_status (IN_PROGRESS → COMPLETED / FAILED / CANCELED).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/formalize",
            body=maybe_transform({"max_prompts": max_prompts}, formalize_create_params.FormalizeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormalizeCreateResponse,
        )

    def delete_all(
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
        """Cancel an in-progress formalization.

        Sets formalization_status to CANCELED.

        If the background task is still running
        it will be interrupted. Idempotent: safe to call even if already COMPLETED.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._delete(
            f"/api/contracts/{contract_id}/formalize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncFormalizeResource(AsyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> AsyncFormalizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFormalizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFormalizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#with_streaming_response
        """
        return AsyncFormalizeResourceWithStreamingResponse(self)

    async def create(
        self,
        contract_id: str,
        *,
        max_prompts: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormalizeCreateResponse:
        """
        Start background formalization of a contract document into Catala code.

        Returns 202 Accepted immediately. Poll GET /{contract_id} for
        formalization_status (IN_PROGRESS → COMPLETED / FAILED / CANCELED).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/formalize",
            body=await async_maybe_transform(
                {"max_prompts": max_prompts}, formalize_create_params.FormalizeCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormalizeCreateResponse,
        )

    async def delete_all(
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
        """Cancel an in-progress formalization.

        Sets formalization_status to CANCELED.

        If the background task is still running
        it will be interrupted. Idempotent: safe to call even if already COMPLETED.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._delete(
            f"/api/contracts/{contract_id}/formalize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class FormalizeResourceWithRawResponse:
    def __init__(self, formalize: FormalizeResource) -> None:
        self._formalize = formalize

        self.create = to_raw_response_wrapper(
            formalize.create,
        )
        self.delete_all = to_raw_response_wrapper(
            formalize.delete_all,
        )


class AsyncFormalizeResourceWithRawResponse:
    def __init__(self, formalize: AsyncFormalizeResource) -> None:
        self._formalize = formalize

        self.create = async_to_raw_response_wrapper(
            formalize.create,
        )
        self.delete_all = async_to_raw_response_wrapper(
            formalize.delete_all,
        )


class FormalizeResourceWithStreamingResponse:
    def __init__(self, formalize: FormalizeResource) -> None:
        self._formalize = formalize

        self.create = to_streamed_response_wrapper(
            formalize.create,
        )
        self.delete_all = to_streamed_response_wrapper(
            formalize.delete_all,
        )


class AsyncFormalizeResourceWithStreamingResponse:
    def __init__(self, formalize: AsyncFormalizeResource) -> None:
        self._formalize = formalize

        self.create = async_to_streamed_response_wrapper(
            formalize.create,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            formalize.delete_all,
        )
