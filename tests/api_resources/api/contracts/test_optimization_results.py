# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptimizationResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_optimization_results(self, client: Formalize) -> None:
        optimization_result = client.api.contracts.optimization_results.delete_optimization_results(
            "contract_id",
        )
        assert_matches_type(object, optimization_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_optimization_results(self, client: Formalize) -> None:
        response = client.api.contracts.optimization_results.with_raw_response.delete_optimization_results(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimization_result = response.parse()
        assert_matches_type(object, optimization_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_optimization_results(self, client: Formalize) -> None:
        with client.api.contracts.optimization_results.with_streaming_response.delete_optimization_results(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimization_result = response.parse()
            assert_matches_type(object, optimization_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_optimization_results(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.optimization_results.with_raw_response.delete_optimization_results(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_optimization_results(self, client: Formalize) -> None:
        optimization_result = client.api.contracts.optimization_results.retrieve_optimization_results(
            "contract_id",
        )
        assert_matches_type(object, optimization_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_optimization_results(self, client: Formalize) -> None:
        response = client.api.contracts.optimization_results.with_raw_response.retrieve_optimization_results(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimization_result = response.parse()
        assert_matches_type(object, optimization_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_optimization_results(self, client: Formalize) -> None:
        with client.api.contracts.optimization_results.with_streaming_response.retrieve_optimization_results(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimization_result = response.parse()
            assert_matches_type(object, optimization_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_optimization_results(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.optimization_results.with_raw_response.retrieve_optimization_results(
                "",
            )


class TestAsyncOptimizationResults:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_optimization_results(self, async_client: AsyncFormalize) -> None:
        optimization_result = await async_client.api.contracts.optimization_results.delete_optimization_results(
            "contract_id",
        )
        assert_matches_type(object, optimization_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_optimization_results(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.optimization_results.with_raw_response.delete_optimization_results(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimization_result = await response.parse()
        assert_matches_type(object, optimization_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_optimization_results(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.optimization_results.with_streaming_response.delete_optimization_results(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimization_result = await response.parse()
            assert_matches_type(object, optimization_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_optimization_results(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.optimization_results.with_raw_response.delete_optimization_results(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_optimization_results(self, async_client: AsyncFormalize) -> None:
        optimization_result = await async_client.api.contracts.optimization_results.retrieve_optimization_results(
            "contract_id",
        )
        assert_matches_type(object, optimization_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_optimization_results(self, async_client: AsyncFormalize) -> None:
        response = (
            await async_client.api.contracts.optimization_results.with_raw_response.retrieve_optimization_results(
                "contract_id",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimization_result = await response.parse()
        assert_matches_type(object, optimization_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_optimization_results(self, async_client: AsyncFormalize) -> None:
        async with (
            async_client.api.contracts.optimization_results.with_streaming_response.retrieve_optimization_results(
                "contract_id",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimization_result = await response.parse()
            assert_matches_type(object, optimization_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_optimization_results(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.optimization_results.with_raw_response.retrieve_optimization_results(
                "",
            )
