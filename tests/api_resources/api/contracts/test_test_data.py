# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_test_data(self, client: Formalize) -> None:
        test_data = client.api.contracts.test_data.retrieve_test_data(
            contract_id="contract_id",
        )
        assert_matches_type(object, test_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_test_data_with_all_params(self, client: Formalize) -> None:
        test_data = client.api.contracts.test_data.retrieve_test_data(
            contract_id="contract_id",
            dataset_id="dataset_id",
        )
        assert_matches_type(object, test_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_test_data(self, client: Formalize) -> None:
        response = client.api.contracts.test_data.with_raw_response.retrieve_test_data(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_data = response.parse()
        assert_matches_type(object, test_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_test_data(self, client: Formalize) -> None:
        with client.api.contracts.test_data.with_streaming_response.retrieve_test_data(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_data = response.parse()
            assert_matches_type(object, test_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_test_data(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.test_data.with_raw_response.retrieve_test_data(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_data(self, client: Formalize) -> None:
        test_data = client.api.contracts.test_data.test_data(
            contract_id="contract_id",
            file=b"Example data",
        )
        assert_matches_type(object, test_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test_data(self, client: Formalize) -> None:
        response = client.api.contracts.test_data.with_raw_response.test_data(
            contract_id="contract_id",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_data = response.parse()
        assert_matches_type(object, test_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test_data(self, client: Formalize) -> None:
        with client.api.contracts.test_data.with_streaming_response.test_data(
            contract_id="contract_id",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_data = response.parse()
            assert_matches_type(object, test_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test_data(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.test_data.with_raw_response.test_data(
                contract_id="",
                file=b"Example data",
            )


class TestAsyncTestData:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_test_data(self, async_client: AsyncFormalize) -> None:
        test_data = await async_client.api.contracts.test_data.retrieve_test_data(
            contract_id="contract_id",
        )
        assert_matches_type(object, test_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_test_data_with_all_params(self, async_client: AsyncFormalize) -> None:
        test_data = await async_client.api.contracts.test_data.retrieve_test_data(
            contract_id="contract_id",
            dataset_id="dataset_id",
        )
        assert_matches_type(object, test_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_test_data(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.test_data.with_raw_response.retrieve_test_data(
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_data = await response.parse()
        assert_matches_type(object, test_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_test_data(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.test_data.with_streaming_response.retrieve_test_data(
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_data = await response.parse()
            assert_matches_type(object, test_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_test_data(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.test_data.with_raw_response.retrieve_test_data(
                contract_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_data(self, async_client: AsyncFormalize) -> None:
        test_data = await async_client.api.contracts.test_data.test_data(
            contract_id="contract_id",
            file=b"Example data",
        )
        assert_matches_type(object, test_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test_data(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.test_data.with_raw_response.test_data(
            contract_id="contract_id",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_data = await response.parse()
        assert_matches_type(object, test_data, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test_data(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.test_data.with_streaming_response.test_data(
            contract_id="contract_id",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_data = await response.parse()
            assert_matches_type(object, test_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test_data(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.test_data.with_raw_response.test_data(
                contract_id="",
                file=b"Example data",
            )
