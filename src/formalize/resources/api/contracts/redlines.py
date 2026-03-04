# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

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
from ....types.api.contracts import ChangeType, RedlineStatus, redline_create_params, redline_update_params
from ....types.api.contracts.change_type import ChangeType
from ....types.api.contracts.redline_status import RedlineStatus
from ....types.api.contracts.redline_response import RedlineResponse
from ....types.api.contracts.redline_list_response import RedlineListResponse

__all__ = ["RedlinesResource", "AsyncRedlinesResource"]


class RedlinesResource(SyncAPIResource):
    """Track and manage proposed changes to contracts"""

    @cached_property
    def with_raw_response(self) -> RedlinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return RedlinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RedlinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return RedlinesResourceWithStreamingResponse(self)

    def create(
        self,
        contract_id: str,
        *,
        change_type: ChangeType,
        contributor_name: str | Omit = omit,
        explanation: Optional[str] | Omit = omit,
        insertion_anchor_text: Optional[str] | Omit = omit,
        new_text: Optional[str] | Omit = omit,
        old_text: Optional[str] | Omit = omit,
        optimization_context: Optional[Dict[str, object]] | Omit = omit,
        paragraph_index: int | Omit = omit,
        status: RedlineStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedlineResponse:
        """
        Create a new redline (e.g., from AI prompt edit).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/redlines",
            body=maybe_transform(
                {
                    "change_type": change_type,
                    "contributor_name": contributor_name,
                    "explanation": explanation,
                    "insertion_anchor_text": insertion_anchor_text,
                    "new_text": new_text,
                    "old_text": old_text,
                    "optimization_context": optimization_context,
                    "paragraph_index": paragraph_index,
                    "status": status,
                },
                redline_create_params.RedlineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedlineResponse,
        )

    def update(
        self,
        redline_id: str,
        *,
        contract_id: str,
        comment_text: Optional[str] | Omit = omit,
        new_text: Optional[str] | Omit = omit,
        old_text: Optional[str] | Omit = omit,
        status: Optional[RedlineStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedlineResponse:
        """
        Edit Redline Text

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        if not redline_id:
            raise ValueError(f"Expected a non-empty value for `redline_id` but received {redline_id!r}")
        return self._patch(
            f"/api/contracts/{contract_id}/redlines/{redline_id}",
            body=maybe_transform(
                {
                    "comment_text": comment_text,
                    "new_text": new_text,
                    "old_text": old_text,
                    "status": status,
                },
                redline_update_params.RedlineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedlineResponse,
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
    ) -> RedlineListResponse:
        """
        List Redlines

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/redlines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedlineListResponse,
        )

    def delete(
        self,
        redline_id: str,
        *,
        contract_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete Redline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        if not redline_id:
            raise ValueError(f"Expected a non-empty value for `redline_id` but received {redline_id!r}")
        return self._delete(
            f"/api/contracts/{contract_id}/redlines/{redline_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRedlinesResource(AsyncAPIResource):
    """Track and manage proposed changes to contracts"""

    @cached_property
    def with_raw_response(self) -> AsyncRedlinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRedlinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRedlinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return AsyncRedlinesResourceWithStreamingResponse(self)

    async def create(
        self,
        contract_id: str,
        *,
        change_type: ChangeType,
        contributor_name: str | Omit = omit,
        explanation: Optional[str] | Omit = omit,
        insertion_anchor_text: Optional[str] | Omit = omit,
        new_text: Optional[str] | Omit = omit,
        old_text: Optional[str] | Omit = omit,
        optimization_context: Optional[Dict[str, object]] | Omit = omit,
        paragraph_index: int | Omit = omit,
        status: RedlineStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedlineResponse:
        """
        Create a new redline (e.g., from AI prompt edit).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/redlines",
            body=await async_maybe_transform(
                {
                    "change_type": change_type,
                    "contributor_name": contributor_name,
                    "explanation": explanation,
                    "insertion_anchor_text": insertion_anchor_text,
                    "new_text": new_text,
                    "old_text": old_text,
                    "optimization_context": optimization_context,
                    "paragraph_index": paragraph_index,
                    "status": status,
                },
                redline_create_params.RedlineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedlineResponse,
        )

    async def update(
        self,
        redline_id: str,
        *,
        contract_id: str,
        comment_text: Optional[str] | Omit = omit,
        new_text: Optional[str] | Omit = omit,
        old_text: Optional[str] | Omit = omit,
        status: Optional[RedlineStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedlineResponse:
        """
        Edit Redline Text

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        if not redline_id:
            raise ValueError(f"Expected a non-empty value for `redline_id` but received {redline_id!r}")
        return await self._patch(
            f"/api/contracts/{contract_id}/redlines/{redline_id}",
            body=await async_maybe_transform(
                {
                    "comment_text": comment_text,
                    "new_text": new_text,
                    "old_text": old_text,
                    "status": status,
                },
                redline_update_params.RedlineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedlineResponse,
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
    ) -> RedlineListResponse:
        """
        List Redlines

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/redlines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedlineListResponse,
        )

    async def delete(
        self,
        redline_id: str,
        *,
        contract_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete Redline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        if not redline_id:
            raise ValueError(f"Expected a non-empty value for `redline_id` but received {redline_id!r}")
        return await self._delete(
            f"/api/contracts/{contract_id}/redlines/{redline_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RedlinesResourceWithRawResponse:
    def __init__(self, redlines: RedlinesResource) -> None:
        self._redlines = redlines

        self.create = to_raw_response_wrapper(
            redlines.create,
        )
        self.update = to_raw_response_wrapper(
            redlines.update,
        )
        self.list = to_raw_response_wrapper(
            redlines.list,
        )
        self.delete = to_raw_response_wrapper(
            redlines.delete,
        )


class AsyncRedlinesResourceWithRawResponse:
    def __init__(self, redlines: AsyncRedlinesResource) -> None:
        self._redlines = redlines

        self.create = async_to_raw_response_wrapper(
            redlines.create,
        )
        self.update = async_to_raw_response_wrapper(
            redlines.update,
        )
        self.list = async_to_raw_response_wrapper(
            redlines.list,
        )
        self.delete = async_to_raw_response_wrapper(
            redlines.delete,
        )


class RedlinesResourceWithStreamingResponse:
    def __init__(self, redlines: RedlinesResource) -> None:
        self._redlines = redlines

        self.create = to_streamed_response_wrapper(
            redlines.create,
        )
        self.update = to_streamed_response_wrapper(
            redlines.update,
        )
        self.list = to_streamed_response_wrapper(
            redlines.list,
        )
        self.delete = to_streamed_response_wrapper(
            redlines.delete,
        )


class AsyncRedlinesResourceWithStreamingResponse:
    def __init__(self, redlines: AsyncRedlinesResource) -> None:
        self._redlines = redlines

        self.create = async_to_streamed_response_wrapper(
            redlines.create,
        )
        self.update = async_to_streamed_response_wrapper(
            redlines.update,
        )
        self.list = async_to_streamed_response_wrapper(
            redlines.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            redlines.delete,
        )
