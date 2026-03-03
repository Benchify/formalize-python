# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ....types.api.contracts import output_config_update_output_configs_params

__all__ = ["OutputConfigsResource", "AsyncOutputConfigsResource"]


class OutputConfigsResource(SyncAPIResource):
    """Manage test datasets for contract evaluation"""

    @cached_property
    def with_raw_response(self) -> OutputConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#accessing-raw-response-data-eg-headers
        """
        return OutputConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutputConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#with_streaming_response
        """
        return OutputConfigsResourceWithStreamingResponse(self)

    def retrieve_output_configs(
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
        Get output configurations for a contract.

        Returns all available outputs with their current configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/output-configs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_output_configs(
        self,
        contract_id: str,
        *,
        output_configs: Iterable[output_config_update_output_configs_params.OutputConfig],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update output configurations for a contract.

        This allows users to:

        - Enable/disable specific outputs from being displayed
        - Set the desired direction (increase/decrease) for each output
        - Customize display names

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._put(
            f"/api/contracts/{contract_id}/output-configs",
            body=maybe_transform(
                {"output_configs": output_configs},
                output_config_update_output_configs_params.OutputConfigUpdateOutputConfigsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOutputConfigsResource(AsyncAPIResource):
    """Manage test datasets for contract evaluation"""

    @cached_property
    def with_raw_response(self) -> AsyncOutputConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOutputConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutputConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#with_streaming_response
        """
        return AsyncOutputConfigsResourceWithStreamingResponse(self)

    async def retrieve_output_configs(
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
        Get output configurations for a contract.

        Returns all available outputs with their current configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/output-configs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_output_configs(
        self,
        contract_id: str,
        *,
        output_configs: Iterable[output_config_update_output_configs_params.OutputConfig],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update output configurations for a contract.

        This allows users to:

        - Enable/disable specific outputs from being displayed
        - Set the desired direction (increase/decrease) for each output
        - Customize display names

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._put(
            f"/api/contracts/{contract_id}/output-configs",
            body=await async_maybe_transform(
                {"output_configs": output_configs},
                output_config_update_output_configs_params.OutputConfigUpdateOutputConfigsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OutputConfigsResourceWithRawResponse:
    def __init__(self, output_configs: OutputConfigsResource) -> None:
        self._output_configs = output_configs

        self.retrieve_output_configs = to_raw_response_wrapper(
            output_configs.retrieve_output_configs,
        )
        self.update_output_configs = to_raw_response_wrapper(
            output_configs.update_output_configs,
        )


class AsyncOutputConfigsResourceWithRawResponse:
    def __init__(self, output_configs: AsyncOutputConfigsResource) -> None:
        self._output_configs = output_configs

        self.retrieve_output_configs = async_to_raw_response_wrapper(
            output_configs.retrieve_output_configs,
        )
        self.update_output_configs = async_to_raw_response_wrapper(
            output_configs.update_output_configs,
        )


class OutputConfigsResourceWithStreamingResponse:
    def __init__(self, output_configs: OutputConfigsResource) -> None:
        self._output_configs = output_configs

        self.retrieve_output_configs = to_streamed_response_wrapper(
            output_configs.retrieve_output_configs,
        )
        self.update_output_configs = to_streamed_response_wrapper(
            output_configs.update_output_configs,
        )


class AsyncOutputConfigsResourceWithStreamingResponse:
    def __init__(self, output_configs: AsyncOutputConfigsResource) -> None:
        self._output_configs = output_configs

        self.retrieve_output_configs = async_to_streamed_response_wrapper(
            output_configs.retrieve_output_configs,
        )
        self.update_output_configs = async_to_streamed_response_wrapper(
            output_configs.update_output_configs,
        )
