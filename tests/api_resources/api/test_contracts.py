# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContracts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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


class TestAsyncContracts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
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
