# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .audit import (
    AuditResource,
    AsyncAuditResource,
    AuditResourceWithRawResponse,
    AsyncAuditResourceWithRawResponse,
    AuditResourceWithStreamingResponse,
    AsyncAuditResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ContractsResource", "AsyncContractsResource"]


class ContractsResource(SyncAPIResource):
    @cached_property
    def audit(self) -> AuditResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AuditResource(self._client)

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


class AsyncContractsResource(AsyncAPIResource):
    @cached_property
    def audit(self) -> AsyncAuditResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncAuditResource(self._client)

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


class ContractsResourceWithRawResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

    @cached_property
    def audit(self) -> AuditResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AuditResourceWithRawResponse(self._contracts.audit)


class AsyncContractsResourceWithRawResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

    @cached_property
    def audit(self) -> AsyncAuditResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncAuditResourceWithRawResponse(self._contracts.audit)


class ContractsResourceWithStreamingResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

    @cached_property
    def audit(self) -> AuditResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AuditResourceWithStreamingResponse(self._contracts.audit)


class AsyncContractsResourceWithStreamingResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

    @cached_property
    def audit(self) -> AsyncAuditResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncAuditResourceWithStreamingResponse(self._contracts.audit)
