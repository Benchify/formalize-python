# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type
from formalize.types.api.contracts import (
    RedlineResponse,
    RedlineListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRedlines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Formalize) -> None:
        redline = client.api.contracts.redlines.create(
            contract_id="contract_id",
            change_type="INSERTION",
        )
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Formalize) -> None:
        redline = client.api.contracts.redlines.create(
            contract_id="contract_id",
            change_type="INSERTION",
            contributor_name="contributor_name",
            explanation="explanation",
            insertion_anchor_text="insertion_anchor_text",
            new_text="new_text",
            old_text="old_text",
            optimization_context={"foo": "bar"},
            paragraph_index=0,
            status="PENDING",
        )
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Formalize) -> None:
        response = client.api.contracts.redlines.with_raw_response.create(
            contract_id="contract_id",
            change_type="INSERTION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redline = response.parse()
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Formalize) -> None:
        with client.api.contracts.redlines.with_streaming_response.create(
            contract_id="contract_id",
            change_type="INSERTION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redline = response.parse()
            assert_matches_type(RedlineResponse, redline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.redlines.with_raw_response.create(
                contract_id="",
                change_type="INSERTION",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Formalize) -> None:
        redline = client.api.contracts.redlines.update(
            redline_id="redline_id",
            contract_id="contract_id",
        )
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Formalize) -> None:
        redline = client.api.contracts.redlines.update(
            redline_id="redline_id",
            contract_id="contract_id",
            comment_text="comment_text",
            new_text="new_text",
            old_text="old_text",
            status="PENDING",
        )
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Formalize) -> None:
        response = client.api.contracts.redlines.with_raw_response.update(
            redline_id="redline_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redline = response.parse()
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Formalize) -> None:
        with client.api.contracts.redlines.with_streaming_response.update(
            redline_id="redline_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redline = response.parse()
            assert_matches_type(RedlineResponse, redline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.redlines.with_raw_response.update(
                redline_id="redline_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `redline_id` but received ''"):
            client.api.contracts.redlines.with_raw_response.update(
                redline_id="",
                contract_id="contract_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Formalize) -> None:
        redline = client.api.contracts.redlines.list(
            "contract_id",
        )
        assert_matches_type(RedlineListResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Formalize) -> None:
        response = client.api.contracts.redlines.with_raw_response.list(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redline = response.parse()
        assert_matches_type(RedlineListResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Formalize) -> None:
        with client.api.contracts.redlines.with_streaming_response.list(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redline = response.parse()
            assert_matches_type(RedlineListResponse, redline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.redlines.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Formalize) -> None:
        redline = client.api.contracts.redlines.delete(
            redline_id="redline_id",
            contract_id="contract_id",
        )
        assert_matches_type(object, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Formalize) -> None:
        response = client.api.contracts.redlines.with_raw_response.delete(
            redline_id="redline_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redline = response.parse()
        assert_matches_type(object, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Formalize) -> None:
        with client.api.contracts.redlines.with_streaming_response.delete(
            redline_id="redline_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redline = response.parse()
            assert_matches_type(object, redline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.redlines.with_raw_response.delete(
                redline_id="redline_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `redline_id` but received ''"):
            client.api.contracts.redlines.with_raw_response.delete(
                redline_id="",
                contract_id="contract_id",
            )


class TestAsyncRedlines:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFormalize) -> None:
        redline = await async_client.api.contracts.redlines.create(
            contract_id="contract_id",
            change_type="INSERTION",
        )
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFormalize) -> None:
        redline = await async_client.api.contracts.redlines.create(
            contract_id="contract_id",
            change_type="INSERTION",
            contributor_name="contributor_name",
            explanation="explanation",
            insertion_anchor_text="insertion_anchor_text",
            new_text="new_text",
            old_text="old_text",
            optimization_context={"foo": "bar"},
            paragraph_index=0,
            status="PENDING",
        )
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.redlines.with_raw_response.create(
            contract_id="contract_id",
            change_type="INSERTION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redline = await response.parse()
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.redlines.with_streaming_response.create(
            contract_id="contract_id",
            change_type="INSERTION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redline = await response.parse()
            assert_matches_type(RedlineResponse, redline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.redlines.with_raw_response.create(
                contract_id="",
                change_type="INSERTION",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFormalize) -> None:
        redline = await async_client.api.contracts.redlines.update(
            redline_id="redline_id",
            contract_id="contract_id",
        )
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFormalize) -> None:
        redline = await async_client.api.contracts.redlines.update(
            redline_id="redline_id",
            contract_id="contract_id",
            comment_text="comment_text",
            new_text="new_text",
            old_text="old_text",
            status="PENDING",
        )
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.redlines.with_raw_response.update(
            redline_id="redline_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redline = await response.parse()
        assert_matches_type(RedlineResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.redlines.with_streaming_response.update(
            redline_id="redline_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redline = await response.parse()
            assert_matches_type(RedlineResponse, redline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.redlines.with_raw_response.update(
                redline_id="redline_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `redline_id` but received ''"):
            await async_client.api.contracts.redlines.with_raw_response.update(
                redline_id="",
                contract_id="contract_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFormalize) -> None:
        redline = await async_client.api.contracts.redlines.list(
            "contract_id",
        )
        assert_matches_type(RedlineListResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.redlines.with_raw_response.list(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redline = await response.parse()
        assert_matches_type(RedlineListResponse, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.redlines.with_streaming_response.list(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redline = await response.parse()
            assert_matches_type(RedlineListResponse, redline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.redlines.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncFormalize) -> None:
        redline = await async_client.api.contracts.redlines.delete(
            redline_id="redline_id",
            contract_id="contract_id",
        )
        assert_matches_type(object, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.redlines.with_raw_response.delete(
            redline_id="redline_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redline = await response.parse()
        assert_matches_type(object, redline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.redlines.with_streaming_response.delete(
            redline_id="redline_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redline = await response.parse()
            assert_matches_type(object, redline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.redlines.with_raw_response.delete(
                redline_id="redline_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `redline_id` but received ''"):
            await async_client.api.contracts.redlines.with_raw_response.delete(
                redline_id="",
                contract_id="contract_id",
            )
