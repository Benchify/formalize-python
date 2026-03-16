# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type
from formalize.types.api.v1.contracts import SpecListResponse, SpecCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpec:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Formalize) -> None:
        spec = client.api.v1.contracts.spec.create(
            contract_id="contract_id",
            model_code="# Contract Formalization\n\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n",
        )
        assert_matches_type(SpecCreateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Formalize) -> None:
        spec = client.api.v1.contracts.spec.create(
            contract_id="contract_id",
            model_code="# Contract Formalization\n\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n",
            validate_syntax=True,
        )
        assert_matches_type(SpecCreateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Formalize) -> None:
        response = client.api.v1.contracts.spec.with_raw_response.create(
            contract_id="contract_id",
            model_code="# Contract Formalization\n\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spec = response.parse()
        assert_matches_type(SpecCreateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Formalize) -> None:
        with client.api.v1.contracts.spec.with_streaming_response.create(
            contract_id="contract_id",
            model_code="# Contract Formalization\n\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spec = response.parse()
            assert_matches_type(SpecCreateResponse, spec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.v1.contracts.spec.with_raw_response.create(
                contract_id="",
                model_code="# Contract Formalization\n\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Formalize) -> None:
        spec = client.api.v1.contracts.spec.list(
            "contract_id",
        )
        assert_matches_type(SpecListResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Formalize) -> None:
        response = client.api.v1.contracts.spec.with_raw_response.list(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spec = response.parse()
        assert_matches_type(SpecListResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Formalize) -> None:
        with client.api.v1.contracts.spec.with_streaming_response.list(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spec = response.parse()
            assert_matches_type(SpecListResponse, spec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.v1.contracts.spec.with_raw_response.list(
                "",
            )


class TestAsyncSpec:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFormalize) -> None:
        spec = await async_client.api.v1.contracts.spec.create(
            contract_id="contract_id",
            model_code="# Contract Formalization\n\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n",
        )
        assert_matches_type(SpecCreateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFormalize) -> None:
        spec = await async_client.api.v1.contracts.spec.create(
            contract_id="contract_id",
            model_code="# Contract Formalization\n\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n",
            validate_syntax=True,
        )
        assert_matches_type(SpecCreateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.contracts.spec.with_raw_response.create(
            contract_id="contract_id",
            model_code="# Contract Formalization\n\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spec = await response.parse()
        assert_matches_type(SpecCreateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.contracts.spec.with_streaming_response.create(
            contract_id="contract_id",
            model_code="# Contract Formalization\n\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spec = await response.parse()
            assert_matches_type(SpecCreateResponse, spec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.v1.contracts.spec.with_raw_response.create(
                contract_id="",
                model_code="# Contract Formalization\n\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFormalize) -> None:
        spec = await async_client.api.v1.contracts.spec.list(
            "contract_id",
        )
        assert_matches_type(SpecListResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.contracts.spec.with_raw_response.list(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spec = await response.parse()
        assert_matches_type(SpecListResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.contracts.spec.with_streaming_response.list(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spec = await response.parse()
            assert_matches_type(SpecListResponse, spec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.v1.contracts.spec.with_raw_response.list(
                "",
            )
