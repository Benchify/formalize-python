# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOutputConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_output_configs(self, client: Formalize) -> None:
        output_config = client.api.contracts.output_configs.retrieve_output_configs(
            "contract_id",
        )
        assert_matches_type(object, output_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_output_configs(self, client: Formalize) -> None:
        response = client.api.contracts.output_configs.with_raw_response.retrieve_output_configs(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output_config = response.parse()
        assert_matches_type(object, output_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_output_configs(self, client: Formalize) -> None:
        with client.api.contracts.output_configs.with_streaming_response.retrieve_output_configs(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output_config = response.parse()
            assert_matches_type(object, output_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_output_configs(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.output_configs.with_raw_response.retrieve_output_configs(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_output_configs(self, client: Formalize) -> None:
        output_config = client.api.contracts.output_configs.update_output_configs(
            contract_id="contract_id",
            output_configs=[{"name": "name"}],
        )
        assert_matches_type(object, output_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_output_configs(self, client: Formalize) -> None:
        response = client.api.contracts.output_configs.with_raw_response.update_output_configs(
            contract_id="contract_id",
            output_configs=[{"name": "name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output_config = response.parse()
        assert_matches_type(object, output_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_output_configs(self, client: Formalize) -> None:
        with client.api.contracts.output_configs.with_streaming_response.update_output_configs(
            contract_id="contract_id",
            output_configs=[{"name": "name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output_config = response.parse()
            assert_matches_type(object, output_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_output_configs(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.output_configs.with_raw_response.update_output_configs(
                contract_id="",
                output_configs=[{"name": "name"}],
            )


class TestAsyncOutputConfigs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_output_configs(self, async_client: AsyncFormalize) -> None:
        output_config = await async_client.api.contracts.output_configs.retrieve_output_configs(
            "contract_id",
        )
        assert_matches_type(object, output_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_output_configs(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.output_configs.with_raw_response.retrieve_output_configs(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output_config = await response.parse()
        assert_matches_type(object, output_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_output_configs(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.output_configs.with_streaming_response.retrieve_output_configs(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output_config = await response.parse()
            assert_matches_type(object, output_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_output_configs(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.output_configs.with_raw_response.retrieve_output_configs(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_output_configs(self, async_client: AsyncFormalize) -> None:
        output_config = await async_client.api.contracts.output_configs.update_output_configs(
            contract_id="contract_id",
            output_configs=[{"name": "name"}],
        )
        assert_matches_type(object, output_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_output_configs(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.output_configs.with_raw_response.update_output_configs(
            contract_id="contract_id",
            output_configs=[{"name": "name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output_config = await response.parse()
        assert_matches_type(object, output_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_output_configs(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.output_configs.with_streaming_response.update_output_configs(
            contract_id="contract_id",
            output_configs=[{"name": "name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output_config = await response.parse()
            assert_matches_type(object, output_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_output_configs(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.output_configs.with_raw_response.update_output_configs(
                contract_id="",
                output_configs=[{"name": "name"}],
            )
