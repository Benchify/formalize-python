# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
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
from .....types.api.contracts.datasets import column_mapping_update_column_mappings_params

__all__ = ["ColumnMappingsResource", "AsyncColumnMappingsResource"]


class ColumnMappingsResource(SyncAPIResource):
    """Manage test datasets for contract evaluation"""

    @cached_property
    def with_raw_response(self) -> ColumnMappingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#accessing-raw-response-data-eg-headers
        """
        return ColumnMappingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ColumnMappingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#with_streaming_response
        """
        return ColumnMappingsResourceWithStreamingResponse(self)

    def retrieve_column_mappings(
        self,
        dataset_id: str,
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
        Return fuzzy-match suggestions and any saved mappings for a dataset.

        Suggestions are computed on the fly by comparing the dataset's Excel headers
        against the Catala scope schema extracted from the contract's current
        catala_code. Saved user overrides are layered on top.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/datasets/{dataset_id}/column-mappings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_column_mappings(
        self,
        dataset_id: str,
        *,
        contract_id: str,
        mappings: Dict[str, Optional[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Persist user-confirmed column mappings for a dataset.

        For named datasets mappings are stored in
        `test_dataset.metadata["column_mappings"]`. For the legacy dataset they are
        stored in `contract_document.contract_metadata["legacy_column_mappings"]`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._put(
            f"/api/contracts/{contract_id}/datasets/{dataset_id}/column-mappings",
            body=maybe_transform(
                {"mappings": mappings},
                column_mapping_update_column_mappings_params.ColumnMappingUpdateColumnMappingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncColumnMappingsResource(AsyncAPIResource):
    """Manage test datasets for contract evaluation"""

    @cached_property
    def with_raw_response(self) -> AsyncColumnMappingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncColumnMappingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncColumnMappingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/formalize-python#with_streaming_response
        """
        return AsyncColumnMappingsResourceWithStreamingResponse(self)

    async def retrieve_column_mappings(
        self,
        dataset_id: str,
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
        Return fuzzy-match suggestions and any saved mappings for a dataset.

        Suggestions are computed on the fly by comparing the dataset's Excel headers
        against the Catala scope schema extracted from the contract's current
        catala_code. Saved user overrides are layered on top.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/datasets/{dataset_id}/column-mappings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_column_mappings(
        self,
        dataset_id: str,
        *,
        contract_id: str,
        mappings: Dict[str, Optional[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Persist user-confirmed column mappings for a dataset.

        For named datasets mappings are stored in
        `test_dataset.metadata["column_mappings"]`. For the legacy dataset they are
        stored in `contract_document.contract_metadata["legacy_column_mappings"]`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._put(
            f"/api/contracts/{contract_id}/datasets/{dataset_id}/column-mappings",
            body=await async_maybe_transform(
                {"mappings": mappings},
                column_mapping_update_column_mappings_params.ColumnMappingUpdateColumnMappingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ColumnMappingsResourceWithRawResponse:
    def __init__(self, column_mappings: ColumnMappingsResource) -> None:
        self._column_mappings = column_mappings

        self.retrieve_column_mappings = to_raw_response_wrapper(
            column_mappings.retrieve_column_mappings,
        )
        self.update_column_mappings = to_raw_response_wrapper(
            column_mappings.update_column_mappings,
        )


class AsyncColumnMappingsResourceWithRawResponse:
    def __init__(self, column_mappings: AsyncColumnMappingsResource) -> None:
        self._column_mappings = column_mappings

        self.retrieve_column_mappings = async_to_raw_response_wrapper(
            column_mappings.retrieve_column_mappings,
        )
        self.update_column_mappings = async_to_raw_response_wrapper(
            column_mappings.update_column_mappings,
        )


class ColumnMappingsResourceWithStreamingResponse:
    def __init__(self, column_mappings: ColumnMappingsResource) -> None:
        self._column_mappings = column_mappings

        self.retrieve_column_mappings = to_streamed_response_wrapper(
            column_mappings.retrieve_column_mappings,
        )
        self.update_column_mappings = to_streamed_response_wrapper(
            column_mappings.update_column_mappings,
        )


class AsyncColumnMappingsResourceWithStreamingResponse:
    def __init__(self, column_mappings: AsyncColumnMappingsResource) -> None:
        self._column_mappings = column_mappings

        self.retrieve_column_mappings = async_to_streamed_response_wrapper(
            column_mappings.retrieve_column_mappings,
        )
        self.update_column_mappings = async_to_streamed_response_wrapper(
            column_mappings.update_column_mappings,
        )
