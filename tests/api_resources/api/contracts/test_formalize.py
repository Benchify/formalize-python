# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type
from formalize.types.api.contracts import FormalizeCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFormalize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Formalize) -> None:
        formalize = client.api.contracts.formalize.create(
            contract_id="contract_id",
        )
        assert_matches_type(FormalizeCreateResponse, formalize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Formalize) -> None:
        formalize = client.api.contracts.formalize.create(
            contract_id="contract_id",
            max_prompts=0,
        )
        assert_matches_type(FormalizeCreateResponse, formalize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Formalize) -> None:
        response = client.api.contracts.formalize.with_raw_response.create(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        formalize = response.parse()
        assert_matches_type(FormalizeCreateResponse, formalize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Formalize) -> None:
        with client.api.contracts.formalize.with_streaming_response.create(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            formalize = response.parse()
            assert_matches_type(FormalizeCreateResponse, formalize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.formalize.with_raw_response.create(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Formalize) -> None:
        formalize = client.api.contracts.formalize.delete_all(
            "contract_id",
        )
        assert_matches_type(object, formalize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Formalize) -> None:
        response = client.api.contracts.formalize.with_raw_response.delete_all(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        formalize = response.parse()
        assert_matches_type(object, formalize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Formalize) -> None:
        with client.api.contracts.formalize.with_streaming_response.delete_all(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            formalize = response.parse()
            assert_matches_type(object, formalize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_all(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.formalize.with_raw_response.delete_all(
                "",
            )


class TestAsyncFormalize:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFormalize) -> None:
        formalize = await async_client.api.contracts.formalize.create(
            contract_id="contract_id",
        )
        assert_matches_type(FormalizeCreateResponse, formalize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFormalize) -> None:
        formalize = await async_client.api.contracts.formalize.create(
            contract_id="contract_id",
            max_prompts=0,
        )
        assert_matches_type(FormalizeCreateResponse, formalize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.formalize.with_raw_response.create(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        formalize = await response.parse()
        assert_matches_type(FormalizeCreateResponse, formalize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.formalize.with_streaming_response.create(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            formalize = await response.parse()
            assert_matches_type(FormalizeCreateResponse, formalize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.formalize.with_raw_response.create(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncFormalize) -> None:
        formalize = await async_client.api.contracts.formalize.delete_all(
            "contract_id",
        )
        assert_matches_type(object, formalize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.formalize.with_raw_response.delete_all(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        formalize = await response.parse()
        assert_matches_type(object, formalize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.formalize.with_streaming_response.delete_all(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            formalize = await response.parse()
            assert_matches_type(object, formalize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.formalize.with_raw_response.delete_all(
                "",
            )
