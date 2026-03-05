# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.api.contracts import persona_update_selected_params

__all__ = ["PersonasResource", "AsyncPersonasResource"]


class PersonasResource(SyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> PersonasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return PersonasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return PersonasResourceWithStreamingResponse(self)

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
        """Get contract personas.

        Infers them from the contract if not yet cached.

        Returns: {personas: [...], selected_persona: str|null}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/personas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def infer(
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
        Force re-run AI persona inference (ignores cache).

        Returns: {personas: [...], selected_persona: str|null}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/personas/infer",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_selected(
        self,
        contract_id: str,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Set the selected persona and update output_configs directions.

        Body: {persona_name: str} Returns: the selected persona dict

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._put(
            f"/api/contracts/{contract_id}/personas/selected",
            body=maybe_transform(body, persona_update_selected_params.PersonaUpdateSelectedParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPersonasResource(AsyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> AsyncPersonasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPersonasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return AsyncPersonasResourceWithStreamingResponse(self)

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
        """Get contract personas.

        Infers them from the contract if not yet cached.

        Returns: {personas: [...], selected_persona: str|null}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/personas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def infer(
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
        Force re-run AI persona inference (ignores cache).

        Returns: {personas: [...], selected_persona: str|null}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/personas/infer",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_selected(
        self,
        contract_id: str,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Set the selected persona and update output_configs directions.

        Body: {persona_name: str} Returns: the selected persona dict

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._put(
            f"/api/contracts/{contract_id}/personas/selected",
            body=await async_maybe_transform(body, persona_update_selected_params.PersonaUpdateSelectedParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PersonasResourceWithRawResponse:
    def __init__(self, personas: PersonasResource) -> None:
        self._personas = personas

        self.list = to_raw_response_wrapper(
            personas.list,
        )
        self.infer = to_raw_response_wrapper(
            personas.infer,
        )
        self.update_selected = to_raw_response_wrapper(
            personas.update_selected,
        )


class AsyncPersonasResourceWithRawResponse:
    def __init__(self, personas: AsyncPersonasResource) -> None:
        self._personas = personas

        self.list = async_to_raw_response_wrapper(
            personas.list,
        )
        self.infer = async_to_raw_response_wrapper(
            personas.infer,
        )
        self.update_selected = async_to_raw_response_wrapper(
            personas.update_selected,
        )


class PersonasResourceWithStreamingResponse:
    def __init__(self, personas: PersonasResource) -> None:
        self._personas = personas

        self.list = to_streamed_response_wrapper(
            personas.list,
        )
        self.infer = to_streamed_response_wrapper(
            personas.infer,
        )
        self.update_selected = to_streamed_response_wrapper(
            personas.update_selected,
        )


class AsyncPersonasResourceWithStreamingResponse:
    def __init__(self, personas: AsyncPersonasResource) -> None:
        self._personas = personas

        self.list = async_to_streamed_response_wrapper(
            personas.list,
        )
        self.infer = async_to_streamed_response_wrapper(
            personas.infer,
        )
        self.update_selected = async_to_streamed_response_wrapper(
            personas.update_selected,
        )
