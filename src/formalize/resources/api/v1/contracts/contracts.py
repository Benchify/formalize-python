# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Optional, cast

import httpx

from .docx import (
    DocxResource,
    AsyncDocxResource,
    DocxResourceWithRawResponse,
    AsyncDocxResourceWithRawResponse,
    DocxResourceWithStreamingResponse,
    AsyncDocxResourceWithStreamingResponse,
)
from .spec import (
    SpecResource,
    AsyncSpecResource,
    SpecResourceWithRawResponse,
    AsyncSpecResourceWithRawResponse,
    SpecResourceWithStreamingResponse,
    AsyncSpecResourceWithStreamingResponse,
)
from .audit import (
    AuditResource,
    AsyncAuditResource,
    AuditResourceWithRawResponse,
    AsyncAuditResourceWithRawResponse,
    AuditResourceWithStreamingResponse,
    AsyncAuditResourceWithStreamingResponse,
)
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
from .....types.api.v1 import (
    FormalizationStatus,
    contract_list_params,
    contract_create_params,
    contract_export_params,
    contract_update_metadata_params,
)
from .....types.api.v1.formalization_status import FormalizationStatus
from .....types.api.v1.contract_list_response import ContractListResponse
from .....types.api.v1.contract_create_response import ContractCreateResponse
from .....types.api.v1.contract_export_response import ContractExportResponse
from .....types.api.v1.contract_retrieve_response import ContractRetrieveResponse
from .....types.api.v1.contract_retrieve_schema_response import ContractRetrieveSchemaResponse
from .....types.api.v1.contract_update_metadata_response import ContractUpdateMetadataResponse
from .....types.api.v1.contract_retrieve_computations_response import ContractRetrieveComputationsResponse
from .....types.api.v1.contract_retrieve_dependencies_response import ContractRetrieveDependenciesResponse

__all__ = ["ContractsResource", "AsyncContractsResource"]


class ContractsResource(SyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def audit(self) -> AuditResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AuditResource(self._client)

    @cached_property
    def spec(self) -> SpecResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return SpecResource(self._client)

    @cached_property
    def docx(self) -> DocxResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return DocxResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return ContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return ContractsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        docx_base64: str,
        filename: str,
        document_title: Optional[str] | Omit = omit,
        model_code: Optional[str] | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractCreateResponse:
        """
        Create a new contract by uploading a DOCX document.

        Args:
          docx_base64: Base64-encoded content of the DOCX file

          filename: Original filename of the DOCX document

          document_title: Human-readable title. If not provided, will be extracted from DOCX.

          model_code: Optional pre-existing formalization code

          org_id: Organization ID to associate with this contract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/contracts",
            body=maybe_transform(
                {
                    "docx_base64": docx_base64,
                    "filename": filename,
                    "document_title": document_title,
                    "model_code": model_code,
                    "org_id": org_id,
                },
                contract_create_params.ContractCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCreateResponse,
        )

    def retrieve(
        self,
        type_name: str,
        *,
        contract_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveResponse:
        """
        Get the definition of a specific type used in a contract.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/v1/contracts/{contract_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        status: Optional[FormalizationStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractListResponse:
        """List all contracts for an organization.

        Requires authentication.

        Returns contracts for the user's organization. If
        org_id is provided, user must be a member of that org.

        Args:
          limit: Max contracts to return

          offset: Offset for pagination

          org_id: Organization ID. If authenticated, defaults to user's org.

          status: Filter by formalization status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "org_id": org_id,
                        "status": status,
                    },
                    contract_list_params.ContractListParams,
                ),
                security={"bearer_auth": True},
            ),
            cast_to=ContractListResponse,
        )

    def delete(
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
        Delete a contract and all associated data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._delete(
            f"/api/v1/contracts/{contract_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def export(
        self,
        contract_id: str,
        *,
        format: str | Omit = omit,
        include_pending: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractExportResponse:
        """
        Export the contract.

        Args:
          format: Export format: 'docx' or 'pdf'

          include_pending: If true, also include PENDING redlines (as tracked changes)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/v1/contracts/{contract_id}/export",
            body=maybe_transform(
                {
                    "format": format,
                    "include_pending": include_pending,
                },
                contract_export_params.ContractExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractExportResponse,
        )

    def retrieve_computations(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveComputationsResponse:
        """
        Get all runnable computations for a contract.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/v1/contracts/{contract_id}/computations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveComputationsResponse,
        )

    def retrieve_dependencies(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveDependenciesResponse:
        """
        Get the dependency graph showing how variables and scopes connect.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/v1/contracts/{contract_id}/dependencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveDependenciesResponse,
        )

    def retrieve_schema(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveSchemaResponse:
        """
        Get the complete schema for a contract including all scopes and types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/v1/contracts/{contract_id}/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveSchemaResponse,
        )

    def update_metadata(
        self,
        contract_id: str,
        *,
        contract_metadata: Optional[Dict[str, object]] | Omit = omit,
        document_title: Optional[str] | Omit = omit,
        filename: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractUpdateMetadataResponse:
        """
        Update metadata for a contract without changing the DOCX or specification.

        Args:
          contract_metadata: Custom metadata dictionary. Will be merged with existing metadata.

          document_title: Human-readable title for the contract

          filename: Update the stored filename

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._patch(
            f"/api/v1/contracts/{contract_id}/metadata",
            body=maybe_transform(
                {
                    "contract_metadata": contract_metadata,
                    "document_title": document_title,
                    "filename": filename,
                },
                contract_update_metadata_params.ContractUpdateMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractUpdateMetadataResponse,
        )


class AsyncContractsResource(AsyncAPIResource):
    """
    Contract document management - upload, view, delete, and manage contract documents
    """

    @cached_property
    def audit(self) -> AsyncAuditResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncAuditResource(self._client)

    @cached_property
    def spec(self) -> AsyncSpecResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncSpecResource(self._client)

    @cached_property
    def docx(self) -> AsyncDocxResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncDocxResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/formalize-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/formalize-python#with_streaming_response
        """
        return AsyncContractsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        docx_base64: str,
        filename: str,
        document_title: Optional[str] | Omit = omit,
        model_code: Optional[str] | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractCreateResponse:
        """
        Create a new contract by uploading a DOCX document.

        Args:
          docx_base64: Base64-encoded content of the DOCX file

          filename: Original filename of the DOCX document

          document_title: Human-readable title. If not provided, will be extracted from DOCX.

          model_code: Optional pre-existing formalization code

          org_id: Organization ID to associate with this contract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/contracts",
            body=await async_maybe_transform(
                {
                    "docx_base64": docx_base64,
                    "filename": filename,
                    "document_title": document_title,
                    "model_code": model_code,
                    "org_id": org_id,
                },
                contract_create_params.ContractCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCreateResponse,
        )

    async def retrieve(
        self,
        type_name: str,
        *,
        contract_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveResponse:
        """
        Get the definition of a specific type used in a contract.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/v1/contracts/{contract_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        status: Optional[FormalizationStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractListResponse:
        """List all contracts for an organization.

        Requires authentication.

        Returns contracts for the user's organization. If
        org_id is provided, user must be a member of that org.

        Args:
          limit: Max contracts to return

          offset: Offset for pagination

          org_id: Organization ID. If authenticated, defaults to user's org.

          status: Filter by formalization status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "org_id": org_id,
                        "status": status,
                    },
                    contract_list_params.ContractListParams,
                ),
                security={"bearer_auth": True},
            ),
            cast_to=ContractListResponse,
        )

    async def delete(
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
        Delete a contract and all associated data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._delete(
            f"/api/v1/contracts/{contract_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def export(
        self,
        contract_id: str,
        *,
        format: str | Omit = omit,
        include_pending: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractExportResponse:
        """
        Export the contract.

        Args:
          format: Export format: 'docx' or 'pdf'

          include_pending: If true, also include PENDING redlines (as tracked changes)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/v1/contracts/{contract_id}/export",
            body=await async_maybe_transform(
                {
                    "format": format,
                    "include_pending": include_pending,
                },
                contract_export_params.ContractExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractExportResponse,
        )

    async def retrieve_computations(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveComputationsResponse:
        """
        Get all runnable computations for a contract.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/v1/contracts/{contract_id}/computations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveComputationsResponse,
        )

    async def retrieve_dependencies(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveDependenciesResponse:
        """
        Get the dependency graph showing how variables and scopes connect.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/v1/contracts/{contract_id}/dependencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveDependenciesResponse,
        )

    async def retrieve_schema(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveSchemaResponse:
        """
        Get the complete schema for a contract including all scopes and types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/v1/contracts/{contract_id}/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveSchemaResponse,
        )

    async def update_metadata(
        self,
        contract_id: str,
        *,
        contract_metadata: Optional[Dict[str, object]] | Omit = omit,
        document_title: Optional[str] | Omit = omit,
        filename: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractUpdateMetadataResponse:
        """
        Update metadata for a contract without changing the DOCX or specification.

        Args:
          contract_metadata: Custom metadata dictionary. Will be merged with existing metadata.

          document_title: Human-readable title for the contract

          filename: Update the stored filename

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._patch(
            f"/api/v1/contracts/{contract_id}/metadata",
            body=await async_maybe_transform(
                {
                    "contract_metadata": contract_metadata,
                    "document_title": document_title,
                    "filename": filename,
                },
                contract_update_metadata_params.ContractUpdateMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractUpdateMetadataResponse,
        )


class ContractsResourceWithRawResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.create = to_raw_response_wrapper(
            contracts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contracts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            contracts.list,
        )
        self.delete = to_raw_response_wrapper(
            contracts.delete,
        )
        self.export = to_raw_response_wrapper(
            contracts.export,
        )
        self.retrieve_computations = to_raw_response_wrapper(
            contracts.retrieve_computations,
        )
        self.retrieve_dependencies = to_raw_response_wrapper(
            contracts.retrieve_dependencies,
        )
        self.retrieve_schema = to_raw_response_wrapper(
            contracts.retrieve_schema,
        )
        self.update_metadata = to_raw_response_wrapper(
            contracts.update_metadata,
        )

    @cached_property
    def audit(self) -> AuditResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AuditResourceWithRawResponse(self._contracts.audit)

    @cached_property
    def spec(self) -> SpecResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return SpecResourceWithRawResponse(self._contracts.spec)

    @cached_property
    def docx(self) -> DocxResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return DocxResourceWithRawResponse(self._contracts.docx)


class AsyncContractsResourceWithRawResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.create = async_to_raw_response_wrapper(
            contracts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contracts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            contracts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            contracts.delete,
        )
        self.export = async_to_raw_response_wrapper(
            contracts.export,
        )
        self.retrieve_computations = async_to_raw_response_wrapper(
            contracts.retrieve_computations,
        )
        self.retrieve_dependencies = async_to_raw_response_wrapper(
            contracts.retrieve_dependencies,
        )
        self.retrieve_schema = async_to_raw_response_wrapper(
            contracts.retrieve_schema,
        )
        self.update_metadata = async_to_raw_response_wrapper(
            contracts.update_metadata,
        )

    @cached_property
    def audit(self) -> AsyncAuditResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncAuditResourceWithRawResponse(self._contracts.audit)

    @cached_property
    def spec(self) -> AsyncSpecResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncSpecResourceWithRawResponse(self._contracts.spec)

    @cached_property
    def docx(self) -> AsyncDocxResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncDocxResourceWithRawResponse(self._contracts.docx)


class ContractsResourceWithStreamingResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.create = to_streamed_response_wrapper(
            contracts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contracts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            contracts.list,
        )
        self.delete = to_streamed_response_wrapper(
            contracts.delete,
        )
        self.export = to_streamed_response_wrapper(
            contracts.export,
        )
        self.retrieve_computations = to_streamed_response_wrapper(
            contracts.retrieve_computations,
        )
        self.retrieve_dependencies = to_streamed_response_wrapper(
            contracts.retrieve_dependencies,
        )
        self.retrieve_schema = to_streamed_response_wrapper(
            contracts.retrieve_schema,
        )
        self.update_metadata = to_streamed_response_wrapper(
            contracts.update_metadata,
        )

    @cached_property
    def audit(self) -> AuditResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AuditResourceWithStreamingResponse(self._contracts.audit)

    @cached_property
    def spec(self) -> SpecResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return SpecResourceWithStreamingResponse(self._contracts.spec)

    @cached_property
    def docx(self) -> DocxResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return DocxResourceWithStreamingResponse(self._contracts.docx)


class AsyncContractsResourceWithStreamingResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.create = async_to_streamed_response_wrapper(
            contracts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contracts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            contracts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            contracts.delete,
        )
        self.export = async_to_streamed_response_wrapper(
            contracts.export,
        )
        self.retrieve_computations = async_to_streamed_response_wrapper(
            contracts.retrieve_computations,
        )
        self.retrieve_dependencies = async_to_streamed_response_wrapper(
            contracts.retrieve_dependencies,
        )
        self.retrieve_schema = async_to_streamed_response_wrapper(
            contracts.retrieve_schema,
        )
        self.update_metadata = async_to_streamed_response_wrapper(
            contracts.update_metadata,
        )

    @cached_property
    def audit(self) -> AsyncAuditResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncAuditResourceWithStreamingResponse(self._contracts.audit)

    @cached_property
    def spec(self) -> AsyncSpecResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncSpecResourceWithStreamingResponse(self._contracts.spec)

    @cached_property
    def docx(self) -> AsyncDocxResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncDocxResourceWithStreamingResponse(self._contracts.docx)
