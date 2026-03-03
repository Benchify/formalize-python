# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type
from formalize.types.api.v1.contracts import DocxUpdateResponse, DocxGetInfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocx:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Formalize) -> None:
        docx = client.api.v1.contracts.docx.update(
            contract_id="contract_id",
            docx_base64="UEsDBBQAAAAIAA...",
        )
        assert_matches_type(DocxUpdateResponse, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Formalize) -> None:
        docx = client.api.v1.contracts.docx.update(
            contract_id="contract_id",
            docx_base64="UEsDBBQAAAAIAA...",
            document_title="PBM Rebate Agreement - Revised",
            filename="updated_contract_v2.docx",
        )
        assert_matches_type(DocxUpdateResponse, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Formalize) -> None:
        response = client.api.v1.contracts.docx.with_raw_response.update(
            contract_id="contract_id",
            docx_base64="UEsDBBQAAAAIAA...",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docx = response.parse()
        assert_matches_type(DocxUpdateResponse, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Formalize) -> None:
        with client.api.v1.contracts.docx.with_streaming_response.update(
            contract_id="contract_id",
            docx_base64="UEsDBBQAAAAIAA...",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docx = response.parse()
            assert_matches_type(DocxUpdateResponse, docx, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.v1.contracts.docx.with_raw_response.update(
                contract_id="",
                docx_base64="UEsDBBQAAAAIAA...",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download(self, client: Formalize) -> None:
        docx = client.api.v1.contracts.docx.download(
            "contract_id",
        )
        assert_matches_type(object, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_download(self, client: Formalize) -> None:
        response = client.api.v1.contracts.docx.with_raw_response.download(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docx = response.parse()
        assert_matches_type(object, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_download(self, client: Formalize) -> None:
        with client.api.v1.contracts.docx.with_streaming_response.download(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docx = response.parse()
            assert_matches_type(object, docx, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_download(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.v1.contracts.docx.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_info(self, client: Formalize) -> None:
        docx = client.api.v1.contracts.docx.get_info(
            "contract_id",
        )
        assert_matches_type(DocxGetInfoResponse, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_info(self, client: Formalize) -> None:
        response = client.api.v1.contracts.docx.with_raw_response.get_info(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docx = response.parse()
        assert_matches_type(DocxGetInfoResponse, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_info(self, client: Formalize) -> None:
        with client.api.v1.contracts.docx.with_streaming_response.get_info(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docx = response.parse()
            assert_matches_type(DocxGetInfoResponse, docx, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_info(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.v1.contracts.docx.with_raw_response.get_info(
                "",
            )


class TestAsyncDocx:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFormalize) -> None:
        docx = await async_client.api.v1.contracts.docx.update(
            contract_id="contract_id",
            docx_base64="UEsDBBQAAAAIAA...",
        )
        assert_matches_type(DocxUpdateResponse, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFormalize) -> None:
        docx = await async_client.api.v1.contracts.docx.update(
            contract_id="contract_id",
            docx_base64="UEsDBBQAAAAIAA...",
            document_title="PBM Rebate Agreement - Revised",
            filename="updated_contract_v2.docx",
        )
        assert_matches_type(DocxUpdateResponse, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.contracts.docx.with_raw_response.update(
            contract_id="contract_id",
            docx_base64="UEsDBBQAAAAIAA...",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docx = await response.parse()
        assert_matches_type(DocxUpdateResponse, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.contracts.docx.with_streaming_response.update(
            contract_id="contract_id",
            docx_base64="UEsDBBQAAAAIAA...",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docx = await response.parse()
            assert_matches_type(DocxUpdateResponse, docx, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.v1.contracts.docx.with_raw_response.update(
                contract_id="",
                docx_base64="UEsDBBQAAAAIAA...",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download(self, async_client: AsyncFormalize) -> None:
        docx = await async_client.api.v1.contracts.docx.download(
            "contract_id",
        )
        assert_matches_type(object, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_download(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.contracts.docx.with_raw_response.download(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docx = await response.parse()
        assert_matches_type(object, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.contracts.docx.with_streaming_response.download(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docx = await response.parse()
            assert_matches_type(object, docx, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_download(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.v1.contracts.docx.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_info(self, async_client: AsyncFormalize) -> None:
        docx = await async_client.api.v1.contracts.docx.get_info(
            "contract_id",
        )
        assert_matches_type(DocxGetInfoResponse, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_info(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.contracts.docx.with_raw_response.get_info(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docx = await response.parse()
        assert_matches_type(DocxGetInfoResponse, docx, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_info(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.contracts.docx.with_streaming_response.get_info(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docx = await response.parse()
            assert_matches_type(DocxGetInfoResponse, docx, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_info(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.v1.contracts.docx.with_raw_response.get_info(
                "",
            )
