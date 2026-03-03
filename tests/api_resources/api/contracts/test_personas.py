# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPersonas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Formalize) -> None:
        persona = client.api.contracts.personas.list(
            "contract_id",
        )
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Formalize) -> None:
        response = client.api.contracts.personas.with_raw_response.list(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = response.parse()
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Formalize) -> None:
        with client.api.contracts.personas.with_streaming_response.list(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = response.parse()
            assert_matches_type(object, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.personas.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_infer(self, client: Formalize) -> None:
        persona = client.api.contracts.personas.infer(
            "contract_id",
        )
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_infer(self, client: Formalize) -> None:
        response = client.api.contracts.personas.with_raw_response.infer(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = response.parse()
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_infer(self, client: Formalize) -> None:
        with client.api.contracts.personas.with_streaming_response.infer(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = response.parse()
            assert_matches_type(object, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_infer(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.personas.with_raw_response.infer(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_selected(self, client: Formalize) -> None:
        persona = client.api.contracts.personas.update_selected(
            contract_id="contract_id",
            body={"foo": "bar"},
        )
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_selected(self, client: Formalize) -> None:
        response = client.api.contracts.personas.with_raw_response.update_selected(
            contract_id="contract_id",
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = response.parse()
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_selected(self, client: Formalize) -> None:
        with client.api.contracts.personas.with_streaming_response.update_selected(
            contract_id="contract_id",
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = response.parse()
            assert_matches_type(object, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_selected(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.personas.with_raw_response.update_selected(
                contract_id="",
                body={"foo": "bar"},
            )


class TestAsyncPersonas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFormalize) -> None:
        persona = await async_client.api.contracts.personas.list(
            "contract_id",
        )
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.personas.with_raw_response.list(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = await response.parse()
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.personas.with_streaming_response.list(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = await response.parse()
            assert_matches_type(object, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.personas.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_infer(self, async_client: AsyncFormalize) -> None:
        persona = await async_client.api.contracts.personas.infer(
            "contract_id",
        )
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_infer(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.personas.with_raw_response.infer(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = await response.parse()
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_infer(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.personas.with_streaming_response.infer(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = await response.parse()
            assert_matches_type(object, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_infer(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.personas.with_raw_response.infer(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_selected(self, async_client: AsyncFormalize) -> None:
        persona = await async_client.api.contracts.personas.update_selected(
            contract_id="contract_id",
            body={"foo": "bar"},
        )
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_selected(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.personas.with_raw_response.update_selected(
            contract_id="contract_id",
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persona = await response.parse()
        assert_matches_type(object, persona, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_selected(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.personas.with_streaming_response.update_selected(
            contract_id="contract_id",
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persona = await response.parse()
            assert_matches_type(object, persona, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_selected(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.personas.with_raw_response.update_selected(
                contract_id="",
                body={"foo": "bar"},
            )
