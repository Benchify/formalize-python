# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type
from formalize.types.api import (
    ContractDocument,
    ContractListResponse,
    ContractDiffDocxResponse,
    ContractEditCatalaResponse,
    ContractSaveCatalaResponse,
    ContractWorkingCopyResponse,
    ContractEditFromDocxResponse,
    ContractEditFromTextResponse,
    ContractValidateCatalaResponse,
    ContractRetrieveModelViewResponse,
    ContractRetrieveParagraphsResponse,
    ContractUploadAndFormalizeResponse,
    ContractRetrieveEditSuggestionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContracts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Formalize) -> None:
        contract = client.api.contracts.retrieve(
            "contract_id",
        )
        assert_matches_type(ContractDocument, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.retrieve(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractDocument, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.retrieve(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractDocument, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Formalize) -> None:
        contract = client.api.contracts.list()
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Formalize) -> None:
        contract = client.api.contracts.list(
            limit=0,
            org_id="org_id",
            skip=0,
        )
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractListResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Formalize) -> None:
        contract = client.api.contracts.delete(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.delete(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.delete(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_analyze_opposing(self, client: Formalize) -> None:
        contract = client.api.contracts.analyze_opposing(
            contract_id="contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_analyze_opposing_with_all_params(self, client: Formalize) -> None:
        contract = client.api.contracts.analyze_opposing(
            contract_id="contract_id",
            analysis_concurrency=0,
            num_test_inputs=0,
            output_var="output_var",
            party_position="party_position",
            scope_name="scope_name",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_analyze_opposing(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.analyze_opposing(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_analyze_opposing(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.analyze_opposing(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_analyze_opposing(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.analyze_opposing(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_working_copy_cache(self, client: Formalize) -> None:
        contract = client.api.contracts.delete_working_copy_cache(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_working_copy_cache(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.delete_working_copy_cache(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_working_copy_cache(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.delete_working_copy_cache(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_working_copy_cache(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.delete_working_copy_cache(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_diff_docx(self, client: Formalize) -> None:
        contract = client.api.contracts.diff_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        )
        assert_matches_type(ContractDiffDocxResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_diff_docx(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.diff_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractDiffDocxResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_diff_docx(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.diff_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractDiffDocxResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_diff_docx(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.diff_docx(
                contract_id="",
                file=b"raw file contents",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_edit_catala(self, client: Formalize) -> None:
        contract = client.api.contracts.edit_catala(
            contract_id="contract_id",
            change_description="change_description",
        )
        assert_matches_type(ContractEditCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_edit_catala_with_all_params(self, client: Formalize) -> None:
        contract = client.api.contracts.edit_catala(
            contract_id="contract_id",
            change_description="change_description",
            current_catala="current_catala",
        )
        assert_matches_type(ContractEditCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_edit_catala(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.edit_catala(
            contract_id="contract_id",
            change_description="change_description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractEditCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_edit_catala(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.edit_catala(
            contract_id="contract_id",
            change_description="change_description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractEditCatalaResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_edit_catala(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.edit_catala(
                contract_id="",
                change_description="change_description",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_edit_from_docx(self, client: Formalize) -> None:
        contract = client.api.contracts.edit_from_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        )
        assert_matches_type(ContractEditFromDocxResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_edit_from_docx(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.edit_from_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractEditFromDocxResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_edit_from_docx(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.edit_from_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractEditFromDocxResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_edit_from_docx(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.edit_from_docx(
                contract_id="",
                file=b"raw file contents",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_edit_from_text(self, client: Formalize) -> None:
        contract = client.api.contracts.edit_from_text(
            contract_id="contract_id",
            edited_paragraphs=["string"],
        )
        assert_matches_type(ContractEditFromTextResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_edit_from_text(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.edit_from_text(
            contract_id="contract_id",
            edited_paragraphs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractEditFromTextResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_edit_from_text(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.edit_from_text(
            contract_id="contract_id",
            edited_paragraphs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractEditFromTextResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_edit_from_text(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.edit_from_text(
                contract_id="",
                edited_paragraphs=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_evaluate_row(self, client: Formalize) -> None:
        contract = client.api.contracts.evaluate_row(
            contract_id="contract_id",
            row_data={"foo": "bar"},
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_evaluate_row_with_all_params(self, client: Formalize) -> None:
        contract = client.api.contracts.evaluate_row(
            contract_id="contract_id",
            row_data={"foo": "bar"},
            use_working_copy=True,
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_evaluate_row(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.evaluate_row(
            contract_id="contract_id",
            row_data={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_evaluate_row(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.evaluate_row(
            contract_id="contract_id",
            row_data={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_evaluate_row(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.evaluate_row(
                contract_id="",
                row_data={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export(self, client: Formalize) -> None:
        contract = client.api.contracts.export(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.export(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.export(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_export(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.export(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fix_formalization(self, client: Formalize) -> None:
        contract = client.api.contracts.fix_formalization(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fix_formalization(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.fix_formalization(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fix_formalization(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.fix_formalization(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_fix_formalization(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.fix_formalization(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_optimize(self, client: Formalize) -> None:
        contract = client.api.contracts.optimize(
            contract_id="contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_optimize_with_all_params(self, client: Formalize) -> None:
        contract = client.api.contracts.optimize(
            contract_id="contract_id",
            analysis_concurrency=0,
            num_test_inputs=0,
            output_var="output_var",
            party_position="party_position",
            scope_name="scope_name",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_optimize(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.optimize(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_optimize(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.optimize(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_optimize(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.optimize(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refresh_scope_metadata(self, client: Formalize) -> None:
        contract = client.api.contracts.refresh_scope_metadata(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_refresh_scope_metadata(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.refresh_scope_metadata(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_refresh_scope_metadata(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.refresh_scope_metadata(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_refresh_scope_metadata(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.refresh_scope_metadata(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_catala(self, client: Formalize) -> None:
        contract = client.api.contracts.retrieve_catala(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_catala(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.retrieve_catala(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_catala(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.retrieve_catala(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_catala(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.retrieve_catala(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_docx(self, client: Formalize) -> None:
        contract = client.api.contracts.retrieve_docx(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_docx(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.retrieve_docx(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_docx(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.retrieve_docx(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_docx(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.retrieve_docx(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_edit_suggestions(self, client: Formalize) -> None:
        contract = client.api.contracts.retrieve_edit_suggestions(
            contract_id="contract_id",
        )
        assert_matches_type(ContractRetrieveEditSuggestionsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_edit_suggestions_with_all_params(self, client: Formalize) -> None:
        contract = client.api.contracts.retrieve_edit_suggestions(
            contract_id="contract_id",
            regenerate=True,
        )
        assert_matches_type(ContractRetrieveEditSuggestionsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_edit_suggestions(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.retrieve_edit_suggestions(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractRetrieveEditSuggestionsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_edit_suggestions(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.retrieve_edit_suggestions(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractRetrieveEditSuggestionsResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_edit_suggestions(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.retrieve_edit_suggestions(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_html(self, client: Formalize) -> None:
        contract = client.api.contracts.retrieve_html(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_html(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.retrieve_html(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_html(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.retrieve_html(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_html(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.retrieve_html(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_model_view(self, client: Formalize) -> None:
        contract = client.api.contracts.retrieve_model_view(
            "contract_id",
        )
        assert_matches_type(ContractRetrieveModelViewResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_model_view(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.retrieve_model_view(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractRetrieveModelViewResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_model_view(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.retrieve_model_view(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractRetrieveModelViewResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_model_view(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.retrieve_model_view(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_paragraphs(self, client: Formalize) -> None:
        contract = client.api.contracts.retrieve_paragraphs(
            "contract_id",
        )
        assert_matches_type(ContractRetrieveParagraphsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_paragraphs(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.retrieve_paragraphs(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractRetrieveParagraphsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_paragraphs(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.retrieve_paragraphs(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractRetrieveParagraphsResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_paragraphs(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.retrieve_paragraphs(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_test_data_with_working_copy(self, client: Formalize) -> None:
        contract = client.api.contracts.retrieve_test_data_with_working_copy(
            contract_id="contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_test_data_with_working_copy_with_all_params(self, client: Formalize) -> None:
        contract = client.api.contracts.retrieve_test_data_with_working_copy(
            contract_id="contract_id",
            dataset_id="dataset_id",
            output_var="output_var",
            scope_name="scope_name",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_test_data_with_working_copy(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.retrieve_test_data_with_working_copy(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_test_data_with_working_copy(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.retrieve_test_data_with_working_copy(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_test_data_with_working_copy(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.retrieve_test_data_with_working_copy(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_save_catala(self, client: Formalize) -> None:
        contract = client.api.contracts.save_catala(
            contract_id="contract_id",
            catala_code="catala_code",
        )
        assert_matches_type(ContractSaveCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_save_catala(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.save_catala(
            contract_id="contract_id",
            catala_code="catala_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractSaveCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_save_catala(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.save_catala(
            contract_id="contract_id",
            catala_code="catala_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractSaveCatalaResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_save_catala(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.save_catala(
                contract_id="",
                catala_code="catala_code",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_data_with_preview(self, client: Formalize) -> None:
        contract = client.api.contracts.test_data_with_preview(
            contract_id="contract_id",
            preview_catala="preview_catala",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test_data_with_preview(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.test_data_with_preview(
            contract_id="contract_id",
            preview_catala="preview_catala",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test_data_with_preview(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.test_data_with_preview(
            contract_id="contract_id",
            preview_catala="preview_catala",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test_data_with_preview(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.test_data_with_preview(
                contract_id="",
                preview_catala="preview_catala",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Formalize) -> None:
        contract = client.api.contracts.upload(
            file=b"raw file contents",
        )
        assert_matches_type(ContractDocument, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Formalize) -> None:
        contract = client.api.contracts.upload(
            file=b"raw file contents",
            org_id="org_id",
            side="side",
        )
        assert_matches_type(ContractDocument, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractDocument, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractDocument, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_and_formalize(self, client: Formalize) -> None:
        contract = client.api.contracts.upload_and_formalize(
            file=b"raw file contents",
        )
        assert_matches_type(ContractUploadAndFormalizeResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_and_formalize_with_all_params(self, client: Formalize) -> None:
        contract = client.api.contracts.upload_and_formalize(
            file=b"raw file contents",
            max_prompts=0,
            org_id="org_id",
            side="side",
        )
        assert_matches_type(ContractUploadAndFormalizeResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload_and_formalize(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.upload_and_formalize(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractUploadAndFormalizeResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload_and_formalize(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.upload_and_formalize(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractUploadAndFormalizeResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_catala(self, client: Formalize) -> None:
        contract = client.api.contracts.validate_catala(
            catala_code="catala_code",
        )
        assert_matches_type(ContractValidateCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate_catala(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.validate_catala(
            catala_code="catala_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractValidateCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate_catala(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.validate_catala(
            catala_code="catala_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractValidateCatalaResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_working_copy(self, client: Formalize) -> None:
        contract = client.api.contracts.working_copy(
            contract_id="contract_id",
            redline_ids=["string"],
        )
        assert_matches_type(ContractWorkingCopyResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_working_copy(self, client: Formalize) -> None:
        response = client.api.contracts.with_raw_response.working_copy(
            contract_id="contract_id",
            redline_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractWorkingCopyResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_working_copy(self, client: Formalize) -> None:
        with client.api.contracts.with_streaming_response.working_copy(
            contract_id="contract_id",
            redline_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractWorkingCopyResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_working_copy(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.with_raw_response.working_copy(
                contract_id="",
                redline_ids=["string"],
            )


class TestAsyncContracts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.retrieve(
            "contract_id",
        )
        assert_matches_type(ContractDocument, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.retrieve(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractDocument, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.retrieve(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractDocument, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.list()
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.list(
            limit=0,
            org_id="org_id",
            skip=0,
        )
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractListResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.delete(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.delete(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.delete(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_analyze_opposing(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.analyze_opposing(
            contract_id="contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_analyze_opposing_with_all_params(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.analyze_opposing(
            contract_id="contract_id",
            analysis_concurrency=0,
            num_test_inputs=0,
            output_var="output_var",
            party_position="party_position",
            scope_name="scope_name",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_analyze_opposing(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.analyze_opposing(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_analyze_opposing(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.analyze_opposing(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_analyze_opposing(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.analyze_opposing(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_working_copy_cache(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.delete_working_copy_cache(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_working_copy_cache(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.delete_working_copy_cache(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_working_copy_cache(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.delete_working_copy_cache(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_working_copy_cache(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.delete_working_copy_cache(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_diff_docx(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.diff_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        )
        assert_matches_type(ContractDiffDocxResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_diff_docx(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.diff_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractDiffDocxResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_diff_docx(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.diff_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractDiffDocxResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_diff_docx(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.diff_docx(
                contract_id="",
                file=b"raw file contents",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_edit_catala(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.edit_catala(
            contract_id="contract_id",
            change_description="change_description",
        )
        assert_matches_type(ContractEditCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_edit_catala_with_all_params(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.edit_catala(
            contract_id="contract_id",
            change_description="change_description",
            current_catala="current_catala",
        )
        assert_matches_type(ContractEditCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_edit_catala(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.edit_catala(
            contract_id="contract_id",
            change_description="change_description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractEditCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_edit_catala(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.edit_catala(
            contract_id="contract_id",
            change_description="change_description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractEditCatalaResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_edit_catala(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.edit_catala(
                contract_id="",
                change_description="change_description",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_edit_from_docx(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.edit_from_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        )
        assert_matches_type(ContractEditFromDocxResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_edit_from_docx(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.edit_from_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractEditFromDocxResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_edit_from_docx(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.edit_from_docx(
            contract_id="contract_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractEditFromDocxResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_edit_from_docx(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.edit_from_docx(
                contract_id="",
                file=b"raw file contents",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_edit_from_text(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.edit_from_text(
            contract_id="contract_id",
            edited_paragraphs=["string"],
        )
        assert_matches_type(ContractEditFromTextResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_edit_from_text(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.edit_from_text(
            contract_id="contract_id",
            edited_paragraphs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractEditFromTextResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_edit_from_text(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.edit_from_text(
            contract_id="contract_id",
            edited_paragraphs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractEditFromTextResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_edit_from_text(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.edit_from_text(
                contract_id="",
                edited_paragraphs=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_evaluate_row(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.evaluate_row(
            contract_id="contract_id",
            row_data={"foo": "bar"},
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_evaluate_row_with_all_params(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.evaluate_row(
            contract_id="contract_id",
            row_data={"foo": "bar"},
            use_working_copy=True,
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_evaluate_row(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.evaluate_row(
            contract_id="contract_id",
            row_data={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_evaluate_row(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.evaluate_row(
            contract_id="contract_id",
            row_data={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_evaluate_row(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.evaluate_row(
                contract_id="",
                row_data={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.export(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.export(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.export(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_export(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.export(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fix_formalization(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.fix_formalization(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fix_formalization(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.fix_formalization(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fix_formalization(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.fix_formalization(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_fix_formalization(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.fix_formalization(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_optimize(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.optimize(
            contract_id="contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_optimize_with_all_params(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.optimize(
            contract_id="contract_id",
            analysis_concurrency=0,
            num_test_inputs=0,
            output_var="output_var",
            party_position="party_position",
            scope_name="scope_name",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_optimize(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.optimize(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_optimize(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.optimize(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_optimize(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.optimize(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refresh_scope_metadata(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.refresh_scope_metadata(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_refresh_scope_metadata(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.refresh_scope_metadata(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_refresh_scope_metadata(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.refresh_scope_metadata(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_refresh_scope_metadata(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.refresh_scope_metadata(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_catala(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.retrieve_catala(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_catala(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.retrieve_catala(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_catala(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.retrieve_catala(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_catala(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.retrieve_catala(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_docx(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.retrieve_docx(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_docx(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.retrieve_docx(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_docx(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.retrieve_docx(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_docx(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.retrieve_docx(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_edit_suggestions(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.retrieve_edit_suggestions(
            contract_id="contract_id",
        )
        assert_matches_type(ContractRetrieveEditSuggestionsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_edit_suggestions_with_all_params(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.retrieve_edit_suggestions(
            contract_id="contract_id",
            regenerate=True,
        )
        assert_matches_type(ContractRetrieveEditSuggestionsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_edit_suggestions(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.retrieve_edit_suggestions(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractRetrieveEditSuggestionsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_edit_suggestions(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.retrieve_edit_suggestions(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractRetrieveEditSuggestionsResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_edit_suggestions(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.retrieve_edit_suggestions(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_html(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.retrieve_html(
            "contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_html(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.retrieve_html(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_html(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.retrieve_html(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_html(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.retrieve_html(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_model_view(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.retrieve_model_view(
            "contract_id",
        )
        assert_matches_type(ContractRetrieveModelViewResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_model_view(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.retrieve_model_view(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractRetrieveModelViewResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_model_view(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.retrieve_model_view(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractRetrieveModelViewResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_model_view(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.retrieve_model_view(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_paragraphs(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.retrieve_paragraphs(
            "contract_id",
        )
        assert_matches_type(ContractRetrieveParagraphsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_paragraphs(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.retrieve_paragraphs(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractRetrieveParagraphsResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_paragraphs(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.retrieve_paragraphs(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractRetrieveParagraphsResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_paragraphs(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.retrieve_paragraphs(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_test_data_with_working_copy(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.retrieve_test_data_with_working_copy(
            contract_id="contract_id",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_test_data_with_working_copy_with_all_params(
        self, async_client: AsyncFormalize
    ) -> None:
        contract = await async_client.api.contracts.retrieve_test_data_with_working_copy(
            contract_id="contract_id",
            dataset_id="dataset_id",
            output_var="output_var",
            scope_name="scope_name",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_test_data_with_working_copy(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.retrieve_test_data_with_working_copy(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_test_data_with_working_copy(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.retrieve_test_data_with_working_copy(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_test_data_with_working_copy(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.retrieve_test_data_with_working_copy(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_save_catala(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.save_catala(
            contract_id="contract_id",
            catala_code="catala_code",
        )
        assert_matches_type(ContractSaveCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_save_catala(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.save_catala(
            contract_id="contract_id",
            catala_code="catala_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractSaveCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_save_catala(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.save_catala(
            contract_id="contract_id",
            catala_code="catala_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractSaveCatalaResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_save_catala(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.save_catala(
                contract_id="",
                catala_code="catala_code",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_data_with_preview(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.test_data_with_preview(
            contract_id="contract_id",
            preview_catala="preview_catala",
        )
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test_data_with_preview(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.test_data_with_preview(
            contract_id="contract_id",
            preview_catala="preview_catala",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(object, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test_data_with_preview(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.test_data_with_preview(
            contract_id="contract_id",
            preview_catala="preview_catala",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(object, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test_data_with_preview(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.test_data_with_preview(
                contract_id="",
                preview_catala="preview_catala",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.upload(
            file=b"raw file contents",
        )
        assert_matches_type(ContractDocument, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.upload(
            file=b"raw file contents",
            org_id="org_id",
            side="side",
        )
        assert_matches_type(ContractDocument, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractDocument, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractDocument, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_and_formalize(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.upload_and_formalize(
            file=b"raw file contents",
        )
        assert_matches_type(ContractUploadAndFormalizeResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_and_formalize_with_all_params(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.upload_and_formalize(
            file=b"raw file contents",
            max_prompts=0,
            org_id="org_id",
            side="side",
        )
        assert_matches_type(ContractUploadAndFormalizeResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload_and_formalize(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.upload_and_formalize(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractUploadAndFormalizeResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload_and_formalize(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.upload_and_formalize(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractUploadAndFormalizeResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_catala(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.validate_catala(
            catala_code="catala_code",
        )
        assert_matches_type(ContractValidateCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate_catala(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.validate_catala(
            catala_code="catala_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractValidateCatalaResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate_catala(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.validate_catala(
            catala_code="catala_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractValidateCatalaResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_working_copy(self, async_client: AsyncFormalize) -> None:
        contract = await async_client.api.contracts.working_copy(
            contract_id="contract_id",
            redline_ids=["string"],
        )
        assert_matches_type(ContractWorkingCopyResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_working_copy(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.with_raw_response.working_copy(
            contract_id="contract_id",
            redline_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractWorkingCopyResponse, contract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_working_copy(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.with_streaming_response.working_copy(
            contract_id="contract_id",
            redline_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractWorkingCopyResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_working_copy(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.with_raw_response.working_copy(
                contract_id="",
                redline_ids=["string"],
            )
