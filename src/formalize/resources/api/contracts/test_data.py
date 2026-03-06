# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.contracts import test_data_test_data_params, test_data_retrieve_test_data_params

__all__ = ["TestDataResource", "AsyncTestDataResource"]


class TestDataResource(SyncAPIResource):
    __test__ = False
    """Manage test datasets for contract evaluation"""

    @cached_property
    def with_raw_response(self) -> TestDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return TestDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return TestDataResourceWithStreamingResponse(self)

    def retrieve_test_data(
        self,
        contract_id: str,
        *,
        dataset_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get test scenario data for a contract.

        Returns the test scenarios as JSON (raw Excel rows) for display.

        Args:
          dataset_id: Specific dataset ID to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/test-data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"dataset_id": dataset_id}, test_data_retrieve_test_data_params.TestDataRetrieveTestDataParams
                ),
            ),
            cast_to=object,
        )

    def test_data(
        self,
        contract_id: str,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Upload test scenario file for a contract.

        Accepts .xlsx, .xls, and .csv files.

        CSV files are converted to Excel. Validates
        the uploaded file against the contract's schema and saves it if validation
        passes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/api/contracts/{contract_id}/test-data",
            body=maybe_transform(body, test_data_test_data_params.TestDataTestDataParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncTestDataResource(AsyncAPIResource):
    """Manage test datasets for contract evaluation"""

    @cached_property
    def with_raw_response(self) -> AsyncTestDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return AsyncTestDataResourceWithStreamingResponse(self)

    async def retrieve_test_data(
        self,
        contract_id: str,
        *,
        dataset_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get test scenario data for a contract.

        Returns the test scenarios as JSON (raw Excel rows) for display.

        Args:
          dataset_id: Specific dataset ID to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/test-data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset_id": dataset_id}, test_data_retrieve_test_data_params.TestDataRetrieveTestDataParams
                ),
            ),
            cast_to=object,
        )

    async def test_data(
        self,
        contract_id: str,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Upload test scenario file for a contract.

        Accepts .xlsx, .xls, and .csv files.

        CSV files are converted to Excel. Validates
        the uploaded file against the contract's schema and saves it if validation
        passes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/api/contracts/{contract_id}/test-data",
            body=await async_maybe_transform(body, test_data_test_data_params.TestDataTestDataParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class TestDataResourceWithRawResponse:
    __test__ = False

    def __init__(self, test_data: TestDataResource) -> None:
        self._test_data = test_data

        self.retrieve_test_data = to_raw_response_wrapper(
            test_data.retrieve_test_data,
        )
        self.test_data = to_raw_response_wrapper(
            test_data.test_data,
        )


class AsyncTestDataResourceWithRawResponse:
    def __init__(self, test_data: AsyncTestDataResource) -> None:
        self._test_data = test_data

        self.retrieve_test_data = async_to_raw_response_wrapper(
            test_data.retrieve_test_data,
        )
        self.test_data = async_to_raw_response_wrapper(
            test_data.test_data,
        )


class TestDataResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, test_data: TestDataResource) -> None:
        self._test_data = test_data

        self.retrieve_test_data = to_streamed_response_wrapper(
            test_data.retrieve_test_data,
        )
        self.test_data = to_streamed_response_wrapper(
            test_data.test_data,
        )


class AsyncTestDataResourceWithStreamingResponse:
    def __init__(self, test_data: AsyncTestDataResource) -> None:
        self._test_data = test_data

        self.retrieve_test_data = async_to_streamed_response_wrapper(
            test_data.retrieve_test_data,
        )
        self.test_data = async_to_streamed_response_wrapper(
            test_data.test_data,
        )
