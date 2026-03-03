# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCoverage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Formalize) -> None:
        coverage = client.api.contracts.coverage.create(
            contract_id="contract_id",
        )
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Formalize) -> None:
        coverage = client.api.contracts.coverage.create(
            contract_id="contract_id",
            regenerate=True,
        )
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Formalize) -> None:
        response = client.api.contracts.coverage.with_raw_response.create(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coverage = response.parse()
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Formalize) -> None:
        with client.api.contracts.coverage.with_streaming_response.create(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coverage = response.parse()
            assert_matches_type(object, coverage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.coverage.with_raw_response.create(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Formalize) -> None:
        coverage = client.api.contracts.coverage.list(
            "contract_id",
        )
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Formalize) -> None:
        response = client.api.contracts.coverage.with_raw_response.list(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coverage = response.parse()
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Formalize) -> None:
        with client.api.contracts.coverage.with_streaming_response.list(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coverage = response.parse()
            assert_matches_type(object, coverage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.coverage.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: Formalize) -> None:
        coverage = client.api.contracts.coverage.retrieve_status(
            "contract_id",
        )
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: Formalize) -> None:
        response = client.api.contracts.coverage.with_raw_response.retrieve_status(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coverage = response.parse()
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Formalize) -> None:
        with client.api.contracts.coverage.with_streaming_response.retrieve_status(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coverage = response.parse()
            assert_matches_type(object, coverage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.coverage.with_raw_response.retrieve_status(
                "",
            )


class TestAsyncCoverage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFormalize) -> None:
        coverage = await async_client.api.contracts.coverage.create(
            contract_id="contract_id",
        )
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFormalize) -> None:
        coverage = await async_client.api.contracts.coverage.create(
            contract_id="contract_id",
            regenerate=True,
        )
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.coverage.with_raw_response.create(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coverage = await response.parse()
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.coverage.with_streaming_response.create(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coverage = await response.parse()
            assert_matches_type(object, coverage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.coverage.with_raw_response.create(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFormalize) -> None:
        coverage = await async_client.api.contracts.coverage.list(
            "contract_id",
        )
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.coverage.with_raw_response.list(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coverage = await response.parse()
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.coverage.with_streaming_response.list(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coverage = await response.parse()
            assert_matches_type(object, coverage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.coverage.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncFormalize) -> None:
        coverage = await async_client.api.contracts.coverage.retrieve_status(
            "contract_id",
        )
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.coverage.with_raw_response.retrieve_status(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coverage = await response.parse()
        assert_matches_type(object, coverage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.coverage.with_streaming_response.retrieve_status(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coverage = await response.parse()
            assert_matches_type(object, coverage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.coverage.with_raw_response.retrieve_status(
                "",
            )
