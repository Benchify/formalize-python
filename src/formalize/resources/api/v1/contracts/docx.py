# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from .....types.api.v1.contracts import docx_update_params
from .....types.api.v1.contracts.docx_update_response import DocxUpdateResponse
from .....types.api.v1.contracts.docx_get_info_response import DocxGetInfoResponse

__all__ = ["DocxResource", "AsyncDocxResource"]


class DocxResource(SyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> DocxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return DocxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return DocxResourceWithStreamingResponse(self)

    def update(
        self,
        contract_id: str,
        *,
        docx_base64: str,
        document_title: Optional[str] | Omit = omit,
        filename: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocxUpdateResponse:
        """
        Update the original DOCX document for a contract.

        Args:
          docx_base64: Base64-encoded content of the DOCX file

          document_title: Human-readable title for the document. If not provided, keeps existing or
              extracts from DOCX.

          filename: New filename for the document. If not provided, keeps the existing filename.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._put(
            f"/api/v1/contracts/{contract_id}/docx",
            body=maybe_transform(
                {
                    "docx_base64": docx_base64,
                    "document_title": document_title,
                    "filename": filename,
                },
                docx_update_params.DocxUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocxUpdateResponse,
        )

    def download(
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
        Download the original DOCX document for a contract.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/v1/contracts/{contract_id}/docx/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=object,
        )

    def get_info(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocxGetInfoResponse:
        """
        Get information about the original DOCX document for a contract.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/v1/contracts/{contract_id}/docx",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=DocxGetInfoResponse,
        )


class AsyncDocxResource(AsyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def with_raw_response(self) -> AsyncDocxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return AsyncDocxResourceWithStreamingResponse(self)

    async def update(
        self,
        contract_id: str,
        *,
        docx_base64: str,
        document_title: Optional[str] | Omit = omit,
        filename: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocxUpdateResponse:
        """
        Update the original DOCX document for a contract.

        Args:
          docx_base64: Base64-encoded content of the DOCX file

          document_title: Human-readable title for the document. If not provided, keeps existing or
              extracts from DOCX.

          filename: New filename for the document. If not provided, keeps the existing filename.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._put(
            f"/api/v1/contracts/{contract_id}/docx",
            body=await async_maybe_transform(
                {
                    "docx_base64": docx_base64,
                    "document_title": document_title,
                    "filename": filename,
                },
                docx_update_params.DocxUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocxUpdateResponse,
        )

    async def download(
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
        Download the original DOCX document for a contract.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/v1/contracts/{contract_id}/docx/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=object,
        )

    async def get_info(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocxGetInfoResponse:
        """
        Get information about the original DOCX document for a contract.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/v1/contracts/{contract_id}/docx",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=DocxGetInfoResponse,
        )


class DocxResourceWithRawResponse:
    def __init__(self, docx: DocxResource) -> None:
        self._docx = docx

        self.update = to_raw_response_wrapper(
            docx.update,
        )
        self.download = to_raw_response_wrapper(
            docx.download,
        )
        self.get_info = to_raw_response_wrapper(
            docx.get_info,
        )


class AsyncDocxResourceWithRawResponse:
    def __init__(self, docx: AsyncDocxResource) -> None:
        self._docx = docx

        self.update = async_to_raw_response_wrapper(
            docx.update,
        )
        self.download = async_to_raw_response_wrapper(
            docx.download,
        )
        self.get_info = async_to_raw_response_wrapper(
            docx.get_info,
        )


class DocxResourceWithStreamingResponse:
    def __init__(self, docx: DocxResource) -> None:
        self._docx = docx

        self.update = to_streamed_response_wrapper(
            docx.update,
        )
        self.download = to_streamed_response_wrapper(
            docx.download,
        )
        self.get_info = to_streamed_response_wrapper(
            docx.get_info,
        )


class AsyncDocxResourceWithStreamingResponse:
    def __init__(self, docx: AsyncDocxResource) -> None:
        self._docx = docx

        self.update = async_to_streamed_response_wrapper(
            docx.update,
        )
        self.download = async_to_streamed_response_wrapper(
            docx.download,
        )
        self.get_info = async_to_streamed_response_wrapper(
            docx.get_info,
        )
