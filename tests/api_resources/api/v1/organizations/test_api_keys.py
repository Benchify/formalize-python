# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type
from formalize.types.api.v1.organizations import (
    APIKeyAPIKeysResponse,
    APIKeyRetrieveAPIKeysResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Formalize) -> None:
        api_key = client.api.v1.organizations.api_keys.delete(
            key_id="key_id",
            org_id="org_id",
        )
        assert_matches_type(object, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Formalize) -> None:
        response = client.api.v1.organizations.api_keys.with_raw_response.delete(
            key_id="key_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(object, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Formalize) -> None:
        with client.api.v1.organizations.api_keys.with_streaming_response.delete(
            key_id="key_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(object, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.api.v1.organizations.api_keys.with_raw_response.delete(
                key_id="key_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.api.v1.organizations.api_keys.with_raw_response.delete(
                key_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_api_keys(self, client: Formalize) -> None:
        api_key = client.api.v1.organizations.api_keys.api_keys(
            org_id="org_id",
            name="x",
        )
        assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_api_keys(self, client: Formalize) -> None:
        response = client.api.v1.organizations.api_keys.with_raw_response.api_keys(
            org_id="org_id",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_api_keys(self, client: Formalize) -> None:
        with client.api.v1.organizations.api_keys.with_streaming_response.api_keys(
            org_id="org_id",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_api_keys(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.api.v1.organizations.api_keys.with_raw_response.api_keys(
                org_id="",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_api_keys(self, client: Formalize) -> None:
        api_key = client.api.v1.organizations.api_keys.retrieve_api_keys(
            "org_id",
        )
        assert_matches_type(APIKeyRetrieveAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_api_keys(self, client: Formalize) -> None:
        response = client.api.v1.organizations.api_keys.with_raw_response.retrieve_api_keys(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyRetrieveAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_api_keys(self, client: Formalize) -> None:
        with client.api.v1.organizations.api_keys.with_streaming_response.retrieve_api_keys(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyRetrieveAPIKeysResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_api_keys(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.api.v1.organizations.api_keys.with_raw_response.retrieve_api_keys(
                "",
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncFormalize) -> None:
        api_key = await async_client.api.v1.organizations.api_keys.delete(
            key_id="key_id",
            org_id="org_id",
        )
        assert_matches_type(object, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.organizations.api_keys.with_raw_response.delete(
            key_id="key_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(object, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.organizations.api_keys.with_streaming_response.delete(
            key_id="key_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(object, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.api.v1.organizations.api_keys.with_raw_response.delete(
                key_id="key_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.api.v1.organizations.api_keys.with_raw_response.delete(
                key_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_api_keys(self, async_client: AsyncFormalize) -> None:
        api_key = await async_client.api.v1.organizations.api_keys.api_keys(
            org_id="org_id",
            name="x",
        )
        assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_api_keys(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.organizations.api_keys.with_raw_response.api_keys(
            org_id="org_id",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_api_keys(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.organizations.api_keys.with_streaming_response.api_keys(
            org_id="org_id",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_api_keys(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.api.v1.organizations.api_keys.with_raw_response.api_keys(
                org_id="",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_api_keys(self, async_client: AsyncFormalize) -> None:
        api_key = await async_client.api.v1.organizations.api_keys.retrieve_api_keys(
            "org_id",
        )
        assert_matches_type(APIKeyRetrieveAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_api_keys(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.organizations.api_keys.with_raw_response.retrieve_api_keys(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyRetrieveAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_api_keys(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.organizations.api_keys.with_streaming_response.retrieve_api_keys(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyRetrieveAPIKeysResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_api_keys(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.api.v1.organizations.api_keys.with_raw_response.retrieve_api_keys(
                "",
            )
