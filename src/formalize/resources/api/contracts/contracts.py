# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Mapping, Optional, cast

import httpx

from .coverage import (
    CoverageResource,
    AsyncCoverageResource,
    CoverageResourceWithRawResponse,
    AsyncCoverageResourceWithRawResponse,
    CoverageResourceWithStreamingResponse,
    AsyncCoverageResourceWithStreamingResponse,
)
from .personas import (
    PersonasResource,
    AsyncPersonasResource,
    PersonasResourceWithRawResponse,
    AsyncPersonasResourceWithRawResponse,
    PersonasResourceWithStreamingResponse,
    AsyncPersonasResourceWithStreamingResponse,
)
from .redlines import (
    RedlinesResource,
    AsyncRedlinesResource,
    RedlinesResourceWithRawResponse,
    AsyncRedlinesResourceWithRawResponse,
    RedlinesResourceWithStreamingResponse,
    AsyncRedlinesResourceWithStreamingResponse,
)
from ...._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .formalize import (
    FormalizeResource,
    AsyncFormalizeResource,
    FormalizeResourceWithRawResponse,
    AsyncFormalizeResourceWithRawResponse,
    FormalizeResourceWithStreamingResponse,
    AsyncFormalizeResourceWithStreamingResponse,
)
from .test_data import (
    TestDataResource,
    AsyncTestDataResource,
    TestDataResourceWithRawResponse,
    AsyncTestDataResourceWithRawResponse,
    TestDataResourceWithStreamingResponse,
    AsyncTestDataResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.api import (
    contract_upload_params,
    contract_optimize_params,
    contract_diff_docx_params,
    contract_evaluate_row_params,
    contract_working_copy_params,
    contract_edit_from_docx_params,
    contract_edit_from_text_params,
    contract_analyze_opposing_params,
    contract_upload_and_formalize_params,
    contract_test_data_with_preview_params,
    contract_retrieve_edit_suggestions_params,
    contract_retrieve_test_data_with_working_copy_params,
)
from .output_configs import (
    OutputConfigsResource,
    AsyncOutputConfigsResource,
    OutputConfigsResourceWithRawResponse,
    AsyncOutputConfigsResourceWithRawResponse,
    OutputConfigsResourceWithStreamingResponse,
    AsyncOutputConfigsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .datasets.datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from .optimization_results import (
    OptimizationResultsResource,
    AsyncOptimizationResultsResource,
    OptimizationResultsResourceWithRawResponse,
    AsyncOptimizationResultsResourceWithRawResponse,
    OptimizationResultsResourceWithStreamingResponse,
    AsyncOptimizationResultsResourceWithStreamingResponse,
)
from ....types.api.contract_document import ContractDocument
from ....types.api.contract_diff_docx_response import ContractDiffDocxResponse
from ....types.api.contract_working_copy_response import ContractWorkingCopyResponse
from ....types.api.contract_edit_from_docx_response import ContractEditFromDocxResponse
from ....types.api.contract_edit_from_text_response import ContractEditFromTextResponse
from ....types.api.contract_retrieve_model_view_response import ContractRetrieveModelViewResponse
from ....types.api.contract_retrieve_paragraphs_response import ContractRetrieveParagraphsResponse
from ....types.api.contract_upload_and_formalize_response import ContractUploadAndFormalizeResponse
from ....types.api.contract_retrieve_edit_suggestions_response import ContractRetrieveEditSuggestionsResponse

__all__ = ["ContractsResource", "AsyncContractsResource"]


class ContractsResource(SyncAPIResource):
    @cached_property
    def formalize(self) -> FormalizeResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return FormalizeResource(self._client)

    @cached_property
    def personas(self) -> PersonasResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return PersonasResource(self._client)

    @cached_property
    def coverage(self) -> CoverageResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return CoverageResource(self._client)

    @cached_property
    def redlines(self) -> RedlinesResource:
        """Track and manage proposed changes to contracts"""
        return RedlinesResource(self._client)

    @cached_property
    def optimization_results(self) -> OptimizationResultsResource:
        """Contract optimization and AI-powered redline generation"""
        return OptimizationResultsResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        """Manage test datasets for contract evaluation"""
        return DatasetsResource(self._client)

    @cached_property
    def test_data(self) -> TestDataResource:
        """Manage test datasets for contract evaluation"""
        return TestDataResource(self._client)

    @cached_property
    def output_configs(self) -> OutputConfigsResource:
        """Manage test datasets for contract evaluation"""
        return OutputConfigsResource(self._client)

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

    def retrieve(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractDocument:
        """
        Get Contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractDocument,
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
        Delete Contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._delete(
            f"/api/contracts/{contract_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def analyze_opposing(
        self,
        contract_id: str,
        *,
        analysis_concurrency: int | Omit = omit,
        num_test_inputs: int | Omit = omit,
        output_var: Optional[str] | Omit = omit,
        party_position: str | Omit = omit,
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Analyze opposing counsel's redlines against the contract specification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/analyze-opposing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "analysis_concurrency": analysis_concurrency,
                        "num_test_inputs": num_test_inputs,
                        "output_var": output_var,
                        "party_position": party_position,
                        "scope_name": scope_name,
                    },
                    contract_analyze_opposing_params.ContractAnalyzeOpposingParams,
                ),
            ),
            cast_to=object,
        )

    def delete_working_copy_cache(
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
        Clear the working copy cache for a contract.

        This forces the next request to recompute the working copy from scratch, which
        can help if the cached working copy is corrupted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._delete(
            f"/api/contracts/{contract_id}/working-copy-cache",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def diff_docx(
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
    ) -> ContractDiffDocxResponse:
        """
        Compare an uploaded docx against the original and return detected changes.

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
            f"/api/contracts/{contract_id}/diff-docx",
            body=maybe_transform(body, contract_diff_docx_params.ContractDiffDocxParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractDiffDocxResponse,
        )

    def edit_from_docx(
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
    ) -> ContractEditFromDocxResponse:
        """
        Upload a modified docx, detect changes, and reformalize affected sections.

        Flow:

        1. Diff uploaded docx against the original
        2. Build a batched change description
        3. Apply via apply_change_to_spec with validation
        4. Return the preview (does NOT auto-save — use save-dsl to persist)

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
            f"/api/contracts/{contract_id}/edit-from-docx",
            body=maybe_transform(body, contract_edit_from_docx_params.ContractEditFromDocxParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractEditFromDocxResponse,
        )

    def edit_from_text(
        self,
        contract_id: str,
        *,
        edited_paragraphs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractEditFromTextResponse:
        """
        Diff edited paragraphs against the original docx and reformalize.

        The frontend sends the full list of paragraphs after the user made inline edits.
        The backend diffs them against the original docx paragraphs, maps each detected
        change to a specification edit, and applies them.

        Returns a preview (does NOT auto-save — use save-dsl to persist).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/edit-from-text",
            body=maybe_transform(
                {"edited_paragraphs": edited_paragraphs}, contract_edit_from_text_params.ContractEditFromTextParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractEditFromTextResponse,
        )

    def evaluate_row(
        self,
        contract_id: str,
        *,
        row_data: Dict[str, object],
        use_working_copy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Evaluate a single data row against the contract model and return every variable
        value.

        Uses the existing evaluation pipeline but runs with `trace=True` so we capture
        all intermediate variable assignments, not just final outputs. The raw JSON
        trace values are returned as-is (no conversion) so the frontend can render them
        with full type information (enums, arrays, ...).

        Query wrapper scopes (`Query_*`) are filtered from the response — only the
        model's own scopes are returned.

        Args:
          row_data: The row data to evaluate

          use_working_copy: If True, apply accepted/in-review redlines before evaluating

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/evaluate-row",
            body=maybe_transform(
                {
                    "row_data": row_data,
                    "use_working_copy": use_working_copy,
                },
                contract_evaluate_row_params.ContractEvaluateRowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def export(
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
        Export Contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def optimize(
        self,
        contract_id: str,
        *,
        analysis_concurrency: int | Omit = omit,
        num_test_inputs: int | Omit = omit,
        output_var: Optional[str] | Omit = omit,
        party_position: str | Omit = omit,
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Run Optimization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/optimize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "analysis_concurrency": analysis_concurrency,
                        "num_test_inputs": num_test_inputs,
                        "output_var": output_var,
                        "party_position": party_position,
                        "scope_name": scope_name,
                    },
                    contract_optimize_params.ContractOptimizeParams,
                ),
            ),
            cast_to=object,
        )

    def refresh_scope_metadata(
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
        Re-detect and update scope metadata from the contract's formalization.

        Useful for contracts that were formalized before scope detection was added, or
        when the formalization has been manually edited.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/refresh-scope-metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_docx(
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
        Download Docx

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/docx",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_edit_suggestions(
        self,
        contract_id: str,
        *,
        regenerate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveEditSuggestionsResponse:
        """
        Get AI-generated edit suggestions for a contract.

        Suggestions are generated based on:

        - The contract text and specification code
        - The configured output variable to optimize
        - The desired optimization direction (increase/decrease)

        Suggestions are cached in contract_metadata. Pass regenerate=True to force
        regeneration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/edit-suggestions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"regenerate": regenerate},
                    contract_retrieve_edit_suggestions_params.ContractRetrieveEditSuggestionsParams,
                ),
            ),
            cast_to=ContractRetrieveEditSuggestionsResponse,
        )

    def retrieve_html(
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
        Get Contract Html

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/html",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_model_view(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveModelViewResponse:
        """
        Return a structured model view generated from the contract formalization.

        Organizes the contract's formal model into the document's article/section
        hierarchy with scope schemas, type definitions, and execution order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/model-view",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveModelViewResponse,
        )

    def retrieve_paragraphs(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveParagraphsResponse:
        """
        Return the original docx paragraphs for in-browser editing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._get(
            f"/api/contracts/{contract_id}/paragraphs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveParagraphsResponse,
        )

    def retrieve_test_data_with_working_copy(
        self,
        contract_id: str,
        *,
        dataset_id: Optional[str] | Omit = omit,
        output_var: Optional[str] | Omit = omit,
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get test scenario data with working copy payment calculations.

        This endpoint:

        1. Loads test scenarios from the Excel file (or specified dataset)
        2. Gets accepted + in-review redlines
        3. Applies those redlines to create a "working copy" specification
        4. Evaluates each test scenario against both base and working copy specs
        5. Returns scenarios with both "Payment" and "Working Copy Payment" columns

        Request cancellation:

        - Checks if the client has disconnected and aborts early if so.
        - The frontend uses AbortController to cancel requests when new ones are
          triggered.

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
            f"/api/contracts/{contract_id}/test-data-with-working-copy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_id": dataset_id,
                        "output_var": output_var,
                        "scope_name": scope_name,
                    },
                    contract_retrieve_test_data_with_working_copy_params.ContractRetrieveTestDataWithWorkingCopyParams,
                ),
            ),
            cast_to=object,
        )

    def test_data_with_preview(
        self,
        contract_id: str,
        *,
        preview_model_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Evaluate test scenarios using a preview specification (without saving).

        This endpoint allows the user to test changes before committing them:

        1. Loads test scenarios from the Excel file
        2. Uses the provided preview_model_code as the "working copy" instead of
           applying redlines
        3. Evaluates each test scenario against both base (saved) and preview specs
        4. Returns scenarios with comparison columns

        This does NOT modify the database - it's purely for preview/testing.

        Args:
          preview_model_code: The preview specification code to evaluate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/test-data-with-preview",
            body=maybe_transform(
                {"preview_model_code": preview_model_code},
                contract_test_data_with_preview_params.ContractTestDataWithPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        org_id: Optional[str] | Omit = omit,
        side: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractDocument:
        """
        Upload Contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/contracts/upload",
            body=maybe_transform(body, contract_upload_params.ContractUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "org_id": org_id,
                        "side": side,
                    },
                    contract_upload_params.ContractUploadParams,
                ),
            ),
            cast_to=ContractDocument,
        )

    def upload_and_formalize(
        self,
        *,
        file: FileTypes,
        max_prompts: Optional[int] | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        side: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractUploadAndFormalizeResponse:
        """
        Upload a document and start background formalization.

        Returns 202 Accepted with the created contract immediately. Poll GET
        /contracts/{contract_id} for formalization_status (IN_PROGRESS → COMPLETED /
        FAILED / CANCELED).

        Supports both .docx and .pdf files. PDFs are converted to DOCX for viewing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/contracts/upload-and-formalize",
            body=maybe_transform(body, contract_upload_and_formalize_params.ContractUploadAndFormalizeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "max_prompts": max_prompts,
                        "org_id": org_id,
                        "side": side,
                    },
                    contract_upload_and_formalize_params.ContractUploadAndFormalizeParams,
                ),
                security={},
            ),
            cast_to=ContractUploadAndFormalizeResponse,
        )

    def working_copy(
        self,
        contract_id: str,
        *,
        redline_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractWorkingCopyResponse:
        """
        Preview a working copy of the contract formalization with selected redlines
        applied.

        This endpoint takes a list of redline IDs and applies them sequentially to the
        base formalization, returning a preview of the resulting code.

        The working copy is NOT persisted — it's a preview for the user to review. Use
        POST /{contract_id}/save-dsl to persist the working copy if desired.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return self._post(
            f"/api/contracts/{contract_id}/working-copy",
            body=maybe_transform({"redline_ids": redline_ids}, contract_working_copy_params.ContractWorkingCopyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractWorkingCopyResponse,
        )


class AsyncContractsResource(AsyncAPIResource):
    @cached_property
    def formalize(self) -> AsyncFormalizeResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncFormalizeResource(self._client)

    @cached_property
    def personas(self) -> AsyncPersonasResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncPersonasResource(self._client)

    @cached_property
    def coverage(self) -> AsyncCoverageResource:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncCoverageResource(self._client)

    @cached_property
    def redlines(self) -> AsyncRedlinesResource:
        """Track and manage proposed changes to contracts"""
        return AsyncRedlinesResource(self._client)

    @cached_property
    def optimization_results(self) -> AsyncOptimizationResultsResource:
        """Contract optimization and AI-powered redline generation"""
        return AsyncOptimizationResultsResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        """Manage test datasets for contract evaluation"""
        return AsyncDatasetsResource(self._client)

    @cached_property
    def test_data(self) -> AsyncTestDataResource:
        """Manage test datasets for contract evaluation"""
        return AsyncTestDataResource(self._client)

    @cached_property
    def output_configs(self) -> AsyncOutputConfigsResource:
        """Manage test datasets for contract evaluation"""
        return AsyncOutputConfigsResource(self._client)

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

    async def retrieve(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractDocument:
        """
        Get Contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractDocument,
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
        Delete Contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._delete(
            f"/api/contracts/{contract_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def analyze_opposing(
        self,
        contract_id: str,
        *,
        analysis_concurrency: int | Omit = omit,
        num_test_inputs: int | Omit = omit,
        output_var: Optional[str] | Omit = omit,
        party_position: str | Omit = omit,
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Analyze opposing counsel's redlines against the contract specification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/analyze-opposing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "analysis_concurrency": analysis_concurrency,
                        "num_test_inputs": num_test_inputs,
                        "output_var": output_var,
                        "party_position": party_position,
                        "scope_name": scope_name,
                    },
                    contract_analyze_opposing_params.ContractAnalyzeOpposingParams,
                ),
            ),
            cast_to=object,
        )

    async def delete_working_copy_cache(
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
        Clear the working copy cache for a contract.

        This forces the next request to recompute the working copy from scratch, which
        can help if the cached working copy is corrupted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._delete(
            f"/api/contracts/{contract_id}/working-copy-cache",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def diff_docx(
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
    ) -> ContractDiffDocxResponse:
        """
        Compare an uploaded docx against the original and return detected changes.

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
            f"/api/contracts/{contract_id}/diff-docx",
            body=await async_maybe_transform(body, contract_diff_docx_params.ContractDiffDocxParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractDiffDocxResponse,
        )

    async def edit_from_docx(
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
    ) -> ContractEditFromDocxResponse:
        """
        Upload a modified docx, detect changes, and reformalize affected sections.

        Flow:

        1. Diff uploaded docx against the original
        2. Build a batched change description
        3. Apply via apply_change_to_spec with validation
        4. Return the preview (does NOT auto-save — use save-dsl to persist)

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
            f"/api/contracts/{contract_id}/edit-from-docx",
            body=await async_maybe_transform(body, contract_edit_from_docx_params.ContractEditFromDocxParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractEditFromDocxResponse,
        )

    async def edit_from_text(
        self,
        contract_id: str,
        *,
        edited_paragraphs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractEditFromTextResponse:
        """
        Diff edited paragraphs against the original docx and reformalize.

        The frontend sends the full list of paragraphs after the user made inline edits.
        The backend diffs them against the original docx paragraphs, maps each detected
        change to a specification edit, and applies them.

        Returns a preview (does NOT auto-save — use save-dsl to persist).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/edit-from-text",
            body=await async_maybe_transform(
                {"edited_paragraphs": edited_paragraphs}, contract_edit_from_text_params.ContractEditFromTextParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractEditFromTextResponse,
        )

    async def evaluate_row(
        self,
        contract_id: str,
        *,
        row_data: Dict[str, object],
        use_working_copy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Evaluate a single data row against the contract model and return every variable
        value.

        Uses the existing evaluation pipeline but runs with `trace=True` so we capture
        all intermediate variable assignments, not just final outputs. The raw JSON
        trace values are returned as-is (no conversion) so the frontend can render them
        with full type information (enums, arrays, ...).

        Query wrapper scopes (`Query_*`) are filtered from the response — only the
        model's own scopes are returned.

        Args:
          row_data: The row data to evaluate

          use_working_copy: If True, apply accepted/in-review redlines before evaluating

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/evaluate-row",
            body=await async_maybe_transform(
                {
                    "row_data": row_data,
                    "use_working_copy": use_working_copy,
                },
                contract_evaluate_row_params.ContractEvaluateRowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def export(
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
        Export Contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def optimize(
        self,
        contract_id: str,
        *,
        analysis_concurrency: int | Omit = omit,
        num_test_inputs: int | Omit = omit,
        output_var: Optional[str] | Omit = omit,
        party_position: str | Omit = omit,
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Run Optimization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/optimize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "analysis_concurrency": analysis_concurrency,
                        "num_test_inputs": num_test_inputs,
                        "output_var": output_var,
                        "party_position": party_position,
                        "scope_name": scope_name,
                    },
                    contract_optimize_params.ContractOptimizeParams,
                ),
            ),
            cast_to=object,
        )

    async def refresh_scope_metadata(
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
        Re-detect and update scope metadata from the contract's formalization.

        Useful for contracts that were formalized before scope detection was added, or
        when the formalization has been manually edited.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/refresh-scope-metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_docx(
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
        Download Docx

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/docx",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_edit_suggestions(
        self,
        contract_id: str,
        *,
        regenerate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveEditSuggestionsResponse:
        """
        Get AI-generated edit suggestions for a contract.

        Suggestions are generated based on:

        - The contract text and specification code
        - The configured output variable to optimize
        - The desired optimization direction (increase/decrease)

        Suggestions are cached in contract_metadata. Pass regenerate=True to force
        regeneration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/edit-suggestions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"regenerate": regenerate},
                    contract_retrieve_edit_suggestions_params.ContractRetrieveEditSuggestionsParams,
                ),
            ),
            cast_to=ContractRetrieveEditSuggestionsResponse,
        )

    async def retrieve_html(
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
        Get Contract Html

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/html",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_model_view(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveModelViewResponse:
        """
        Return a structured model view generated from the contract formalization.

        Organizes the contract's formal model into the document's article/section
        hierarchy with scope schemas, type definitions, and execution order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/model-view",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveModelViewResponse,
        )

    async def retrieve_paragraphs(
        self,
        contract_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveParagraphsResponse:
        """
        Return the original docx paragraphs for in-browser editing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._get(
            f"/api/contracts/{contract_id}/paragraphs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveParagraphsResponse,
        )

    async def retrieve_test_data_with_working_copy(
        self,
        contract_id: str,
        *,
        dataset_id: Optional[str] | Omit = omit,
        output_var: Optional[str] | Omit = omit,
        scope_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get test scenario data with working copy payment calculations.

        This endpoint:

        1. Loads test scenarios from the Excel file (or specified dataset)
        2. Gets accepted + in-review redlines
        3. Applies those redlines to create a "working copy" specification
        4. Evaluates each test scenario against both base and working copy specs
        5. Returns scenarios with both "Payment" and "Working Copy Payment" columns

        Request cancellation:

        - Checks if the client has disconnected and aborts early if so.
        - The frontend uses AbortController to cancel requests when new ones are
          triggered.

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
            f"/api/contracts/{contract_id}/test-data-with-working-copy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset_id": dataset_id,
                        "output_var": output_var,
                        "scope_name": scope_name,
                    },
                    contract_retrieve_test_data_with_working_copy_params.ContractRetrieveTestDataWithWorkingCopyParams,
                ),
            ),
            cast_to=object,
        )

    async def test_data_with_preview(
        self,
        contract_id: str,
        *,
        preview_model_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Evaluate test scenarios using a preview specification (without saving).

        This endpoint allows the user to test changes before committing them:

        1. Loads test scenarios from the Excel file
        2. Uses the provided preview_model_code as the "working copy" instead of
           applying redlines
        3. Evaluates each test scenario against both base (saved) and preview specs
        4. Returns scenarios with comparison columns

        This does NOT modify the database - it's purely for preview/testing.

        Args:
          preview_model_code: The preview specification code to evaluate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/test-data-with-preview",
            body=await async_maybe_transform(
                {"preview_model_code": preview_model_code},
                contract_test_data_with_preview_params.ContractTestDataWithPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        org_id: Optional[str] | Omit = omit,
        side: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractDocument:
        """
        Upload Contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/contracts/upload",
            body=await async_maybe_transform(body, contract_upload_params.ContractUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "org_id": org_id,
                        "side": side,
                    },
                    contract_upload_params.ContractUploadParams,
                ),
            ),
            cast_to=ContractDocument,
        )

    async def upload_and_formalize(
        self,
        *,
        file: FileTypes,
        max_prompts: Optional[int] | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        side: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractUploadAndFormalizeResponse:
        """
        Upload a document and start background formalization.

        Returns 202 Accepted with the created contract immediately. Poll GET
        /contracts/{contract_id} for formalization_status (IN_PROGRESS → COMPLETED /
        FAILED / CANCELED).

        Supports both .docx and .pdf files. PDFs are converted to DOCX for viewing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/contracts/upload-and-formalize",
            body=await async_maybe_transform(
                body, contract_upload_and_formalize_params.ContractUploadAndFormalizeParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "max_prompts": max_prompts,
                        "org_id": org_id,
                        "side": side,
                    },
                    contract_upload_and_formalize_params.ContractUploadAndFormalizeParams,
                ),
                security={},
            ),
            cast_to=ContractUploadAndFormalizeResponse,
        )

    async def working_copy(
        self,
        contract_id: str,
        *,
        redline_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractWorkingCopyResponse:
        """
        Preview a working copy of the contract formalization with selected redlines
        applied.

        This endpoint takes a list of redline IDs and applies them sequentially to the
        base formalization, returning a preview of the resulting code.

        The working copy is NOT persisted — it's a preview for the user to review. Use
        POST /{contract_id}/save-dsl to persist the working copy if desired.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contract_id:
            raise ValueError(f"Expected a non-empty value for `contract_id` but received {contract_id!r}")
        return await self._post(
            f"/api/contracts/{contract_id}/working-copy",
            body=await async_maybe_transform(
                {"redline_ids": redline_ids}, contract_working_copy_params.ContractWorkingCopyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractWorkingCopyResponse,
        )


class ContractsResourceWithRawResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.retrieve = to_raw_response_wrapper(
            contracts.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            contracts.delete,
        )
        self.analyze_opposing = to_raw_response_wrapper(
            contracts.analyze_opposing,
        )
        self.delete_working_copy_cache = to_raw_response_wrapper(
            contracts.delete_working_copy_cache,
        )
        self.diff_docx = to_raw_response_wrapper(
            contracts.diff_docx,
        )
        self.edit_from_docx = to_raw_response_wrapper(
            contracts.edit_from_docx,
        )
        self.edit_from_text = to_raw_response_wrapper(
            contracts.edit_from_text,
        )
        self.evaluate_row = to_raw_response_wrapper(
            contracts.evaluate_row,
        )
        self.export = to_raw_response_wrapper(
            contracts.export,
        )
        self.optimize = to_raw_response_wrapper(
            contracts.optimize,
        )
        self.refresh_scope_metadata = to_raw_response_wrapper(
            contracts.refresh_scope_metadata,
        )
        self.retrieve_docx = to_raw_response_wrapper(
            contracts.retrieve_docx,
        )
        self.retrieve_edit_suggestions = to_raw_response_wrapper(
            contracts.retrieve_edit_suggestions,
        )
        self.retrieve_html = to_raw_response_wrapper(
            contracts.retrieve_html,
        )
        self.retrieve_model_view = to_raw_response_wrapper(
            contracts.retrieve_model_view,
        )
        self.retrieve_paragraphs = to_raw_response_wrapper(
            contracts.retrieve_paragraphs,
        )
        self.retrieve_test_data_with_working_copy = to_raw_response_wrapper(
            contracts.retrieve_test_data_with_working_copy,
        )
        self.test_data_with_preview = to_raw_response_wrapper(
            contracts.test_data_with_preview,
        )
        self.upload = to_raw_response_wrapper(
            contracts.upload,
        )
        self.upload_and_formalize = to_raw_response_wrapper(
            contracts.upload_and_formalize,
        )
        self.working_copy = to_raw_response_wrapper(
            contracts.working_copy,
        )

    @cached_property
    def formalize(self) -> FormalizeResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return FormalizeResourceWithRawResponse(self._contracts.formalize)

    @cached_property
    def personas(self) -> PersonasResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return PersonasResourceWithRawResponse(self._contracts.personas)

    @cached_property
    def coverage(self) -> CoverageResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return CoverageResourceWithRawResponse(self._contracts.coverage)

    @cached_property
    def redlines(self) -> RedlinesResourceWithRawResponse:
        """Track and manage proposed changes to contracts"""
        return RedlinesResourceWithRawResponse(self._contracts.redlines)

    @cached_property
    def optimization_results(self) -> OptimizationResultsResourceWithRawResponse:
        """Contract optimization and AI-powered redline generation"""
        return OptimizationResultsResourceWithRawResponse(self._contracts.optimization_results)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        """Manage test datasets for contract evaluation"""
        return DatasetsResourceWithRawResponse(self._contracts.datasets)

    @cached_property
    def test_data(self) -> TestDataResourceWithRawResponse:
        """Manage test datasets for contract evaluation"""
        return TestDataResourceWithRawResponse(self._contracts.test_data)

    @cached_property
    def output_configs(self) -> OutputConfigsResourceWithRawResponse:
        """Manage test datasets for contract evaluation"""
        return OutputConfigsResourceWithRawResponse(self._contracts.output_configs)


class AsyncContractsResourceWithRawResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.retrieve = async_to_raw_response_wrapper(
            contracts.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            contracts.delete,
        )
        self.analyze_opposing = async_to_raw_response_wrapper(
            contracts.analyze_opposing,
        )
        self.delete_working_copy_cache = async_to_raw_response_wrapper(
            contracts.delete_working_copy_cache,
        )
        self.diff_docx = async_to_raw_response_wrapper(
            contracts.diff_docx,
        )
        self.edit_from_docx = async_to_raw_response_wrapper(
            contracts.edit_from_docx,
        )
        self.edit_from_text = async_to_raw_response_wrapper(
            contracts.edit_from_text,
        )
        self.evaluate_row = async_to_raw_response_wrapper(
            contracts.evaluate_row,
        )
        self.export = async_to_raw_response_wrapper(
            contracts.export,
        )
        self.optimize = async_to_raw_response_wrapper(
            contracts.optimize,
        )
        self.refresh_scope_metadata = async_to_raw_response_wrapper(
            contracts.refresh_scope_metadata,
        )
        self.retrieve_docx = async_to_raw_response_wrapper(
            contracts.retrieve_docx,
        )
        self.retrieve_edit_suggestions = async_to_raw_response_wrapper(
            contracts.retrieve_edit_suggestions,
        )
        self.retrieve_html = async_to_raw_response_wrapper(
            contracts.retrieve_html,
        )
        self.retrieve_model_view = async_to_raw_response_wrapper(
            contracts.retrieve_model_view,
        )
        self.retrieve_paragraphs = async_to_raw_response_wrapper(
            contracts.retrieve_paragraphs,
        )
        self.retrieve_test_data_with_working_copy = async_to_raw_response_wrapper(
            contracts.retrieve_test_data_with_working_copy,
        )
        self.test_data_with_preview = async_to_raw_response_wrapper(
            contracts.test_data_with_preview,
        )
        self.upload = async_to_raw_response_wrapper(
            contracts.upload,
        )
        self.upload_and_formalize = async_to_raw_response_wrapper(
            contracts.upload_and_formalize,
        )
        self.working_copy = async_to_raw_response_wrapper(
            contracts.working_copy,
        )

    @cached_property
    def formalize(self) -> AsyncFormalizeResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncFormalizeResourceWithRawResponse(self._contracts.formalize)

    @cached_property
    def personas(self) -> AsyncPersonasResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncPersonasResourceWithRawResponse(self._contracts.personas)

    @cached_property
    def coverage(self) -> AsyncCoverageResourceWithRawResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncCoverageResourceWithRawResponse(self._contracts.coverage)

    @cached_property
    def redlines(self) -> AsyncRedlinesResourceWithRawResponse:
        """Track and manage proposed changes to contracts"""
        return AsyncRedlinesResourceWithRawResponse(self._contracts.redlines)

    @cached_property
    def optimization_results(self) -> AsyncOptimizationResultsResourceWithRawResponse:
        """Contract optimization and AI-powered redline generation"""
        return AsyncOptimizationResultsResourceWithRawResponse(self._contracts.optimization_results)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        """Manage test datasets for contract evaluation"""
        return AsyncDatasetsResourceWithRawResponse(self._contracts.datasets)

    @cached_property
    def test_data(self) -> AsyncTestDataResourceWithRawResponse:
        """Manage test datasets for contract evaluation"""
        return AsyncTestDataResourceWithRawResponse(self._contracts.test_data)

    @cached_property
    def output_configs(self) -> AsyncOutputConfigsResourceWithRawResponse:
        """Manage test datasets for contract evaluation"""
        return AsyncOutputConfigsResourceWithRawResponse(self._contracts.output_configs)


class ContractsResourceWithStreamingResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.retrieve = to_streamed_response_wrapper(
            contracts.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            contracts.delete,
        )
        self.analyze_opposing = to_streamed_response_wrapper(
            contracts.analyze_opposing,
        )
        self.delete_working_copy_cache = to_streamed_response_wrapper(
            contracts.delete_working_copy_cache,
        )
        self.diff_docx = to_streamed_response_wrapper(
            contracts.diff_docx,
        )
        self.edit_from_docx = to_streamed_response_wrapper(
            contracts.edit_from_docx,
        )
        self.edit_from_text = to_streamed_response_wrapper(
            contracts.edit_from_text,
        )
        self.evaluate_row = to_streamed_response_wrapper(
            contracts.evaluate_row,
        )
        self.export = to_streamed_response_wrapper(
            contracts.export,
        )
        self.optimize = to_streamed_response_wrapper(
            contracts.optimize,
        )
        self.refresh_scope_metadata = to_streamed_response_wrapper(
            contracts.refresh_scope_metadata,
        )
        self.retrieve_docx = to_streamed_response_wrapper(
            contracts.retrieve_docx,
        )
        self.retrieve_edit_suggestions = to_streamed_response_wrapper(
            contracts.retrieve_edit_suggestions,
        )
        self.retrieve_html = to_streamed_response_wrapper(
            contracts.retrieve_html,
        )
        self.retrieve_model_view = to_streamed_response_wrapper(
            contracts.retrieve_model_view,
        )
        self.retrieve_paragraphs = to_streamed_response_wrapper(
            contracts.retrieve_paragraphs,
        )
        self.retrieve_test_data_with_working_copy = to_streamed_response_wrapper(
            contracts.retrieve_test_data_with_working_copy,
        )
        self.test_data_with_preview = to_streamed_response_wrapper(
            contracts.test_data_with_preview,
        )
        self.upload = to_streamed_response_wrapper(
            contracts.upload,
        )
        self.upload_and_formalize = to_streamed_response_wrapper(
            contracts.upload_and_formalize,
        )
        self.working_copy = to_streamed_response_wrapper(
            contracts.working_copy,
        )

    @cached_property
    def formalize(self) -> FormalizeResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return FormalizeResourceWithStreamingResponse(self._contracts.formalize)

    @cached_property
    def personas(self) -> PersonasResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return PersonasResourceWithStreamingResponse(self._contracts.personas)

    @cached_property
    def coverage(self) -> CoverageResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return CoverageResourceWithStreamingResponse(self._contracts.coverage)

    @cached_property
    def redlines(self) -> RedlinesResourceWithStreamingResponse:
        """Track and manage proposed changes to contracts"""
        return RedlinesResourceWithStreamingResponse(self._contracts.redlines)

    @cached_property
    def optimization_results(self) -> OptimizationResultsResourceWithStreamingResponse:
        """Contract optimization and AI-powered redline generation"""
        return OptimizationResultsResourceWithStreamingResponse(self._contracts.optimization_results)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        """Manage test datasets for contract evaluation"""
        return DatasetsResourceWithStreamingResponse(self._contracts.datasets)

    @cached_property
    def test_data(self) -> TestDataResourceWithStreamingResponse:
        """Manage test datasets for contract evaluation"""
        return TestDataResourceWithStreamingResponse(self._contracts.test_data)

    @cached_property
    def output_configs(self) -> OutputConfigsResourceWithStreamingResponse:
        """Manage test datasets for contract evaluation"""
        return OutputConfigsResourceWithStreamingResponse(self._contracts.output_configs)


class AsyncContractsResourceWithStreamingResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.retrieve = async_to_streamed_response_wrapper(
            contracts.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            contracts.delete,
        )
        self.analyze_opposing = async_to_streamed_response_wrapper(
            contracts.analyze_opposing,
        )
        self.delete_working_copy_cache = async_to_streamed_response_wrapper(
            contracts.delete_working_copy_cache,
        )
        self.diff_docx = async_to_streamed_response_wrapper(
            contracts.diff_docx,
        )
        self.edit_from_docx = async_to_streamed_response_wrapper(
            contracts.edit_from_docx,
        )
        self.edit_from_text = async_to_streamed_response_wrapper(
            contracts.edit_from_text,
        )
        self.evaluate_row = async_to_streamed_response_wrapper(
            contracts.evaluate_row,
        )
        self.export = async_to_streamed_response_wrapper(
            contracts.export,
        )
        self.optimize = async_to_streamed_response_wrapper(
            contracts.optimize,
        )
        self.refresh_scope_metadata = async_to_streamed_response_wrapper(
            contracts.refresh_scope_metadata,
        )
        self.retrieve_docx = async_to_streamed_response_wrapper(
            contracts.retrieve_docx,
        )
        self.retrieve_edit_suggestions = async_to_streamed_response_wrapper(
            contracts.retrieve_edit_suggestions,
        )
        self.retrieve_html = async_to_streamed_response_wrapper(
            contracts.retrieve_html,
        )
        self.retrieve_model_view = async_to_streamed_response_wrapper(
            contracts.retrieve_model_view,
        )
        self.retrieve_paragraphs = async_to_streamed_response_wrapper(
            contracts.retrieve_paragraphs,
        )
        self.retrieve_test_data_with_working_copy = async_to_streamed_response_wrapper(
            contracts.retrieve_test_data_with_working_copy,
        )
        self.test_data_with_preview = async_to_streamed_response_wrapper(
            contracts.test_data_with_preview,
        )
        self.upload = async_to_streamed_response_wrapper(
            contracts.upload,
        )
        self.upload_and_formalize = async_to_streamed_response_wrapper(
            contracts.upload_and_formalize,
        )
        self.working_copy = async_to_streamed_response_wrapper(
            contracts.working_copy,
        )

    @cached_property
    def formalize(self) -> AsyncFormalizeResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncFormalizeResourceWithStreamingResponse(self._contracts.formalize)

    @cached_property
    def personas(self) -> AsyncPersonasResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncPersonasResourceWithStreamingResponse(self._contracts.personas)

    @cached_property
    def coverage(self) -> AsyncCoverageResourceWithStreamingResponse:
        """
        Contract document management - upload, view, delete, and manage contract documents
        """
        return AsyncCoverageResourceWithStreamingResponse(self._contracts.coverage)

    @cached_property
    def redlines(self) -> AsyncRedlinesResourceWithStreamingResponse:
        """Track and manage proposed changes to contracts"""
        return AsyncRedlinesResourceWithStreamingResponse(self._contracts.redlines)

    @cached_property
    def optimization_results(self) -> AsyncOptimizationResultsResourceWithStreamingResponse:
        """Contract optimization and AI-powered redline generation"""
        return AsyncOptimizationResultsResourceWithStreamingResponse(self._contracts.optimization_results)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """Manage test datasets for contract evaluation"""
        return AsyncDatasetsResourceWithStreamingResponse(self._contracts.datasets)

    @cached_property
    def test_data(self) -> AsyncTestDataResourceWithStreamingResponse:
        """Manage test datasets for contract evaluation"""
        return AsyncTestDataResourceWithStreamingResponse(self._contracts.test_data)

    @cached_property
    def output_configs(self) -> AsyncOutputConfigsResourceWithStreamingResponse:
        """Manage test datasets for contract evaluation"""
        return AsyncOutputConfigsResourceWithStreamingResponse(self._contracts.output_configs)
