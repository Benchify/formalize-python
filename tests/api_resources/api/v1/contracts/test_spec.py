# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type
from formalize.types.api.v1.contracts import SpecGetResponse, SpecUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpec:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Formalize) -> None:
        spec = client.api.v1.contracts.spec.update(
            contract_id="contract_id",
            catala_code="# Contract Formalization\n\n```catala\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n```\n",
        )
        assert_matches_type(SpecUpdateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Formalize) -> None:
        spec = client.api.v1.contracts.spec.update(
            contract_id="contract_id",
            catala_code="# Contract Formalization\n\n```catala\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n```\n",
            validate_syntax=True,
        )
        assert_matches_type(SpecUpdateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Formalize) -> None:
        response = client.api.v1.contracts.spec.with_raw_response.update(
            contract_id="contract_id",
            catala_code="# Contract Formalization\n\n```catala\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n```\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spec = response.parse()
        assert_matches_type(SpecUpdateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Formalize) -> None:
        with client.api.v1.contracts.spec.with_streaming_response.update(
            contract_id="contract_id",
            catala_code="# Contract Formalization\n\n```catala\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n```\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spec = response.parse()
            assert_matches_type(SpecUpdateResponse, spec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.v1.contracts.spec.with_raw_response.update(
                contract_id="",
                catala_code="# Contract Formalization\n\n```catala\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n```\n",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Formalize) -> None:
        spec = client.api.v1.contracts.spec.get(
            "contract_id",
        )
        assert_matches_type(SpecGetResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Formalize) -> None:
        response = client.api.v1.contracts.spec.with_raw_response.get(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spec = response.parse()
        assert_matches_type(SpecGetResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Formalize) -> None:
        with client.api.v1.contracts.spec.with_streaming_response.get(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spec = response.parse()
            assert_matches_type(SpecGetResponse, spec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.v1.contracts.spec.with_raw_response.get(
                "",
            )


class TestAsyncSpec:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFormalize) -> None:
        spec = await async_client.api.v1.contracts.spec.update(
            contract_id="contract_id",
            catala_code="# Contract Formalization\n\n```catala\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n```\n",
        )
        assert_matches_type(SpecUpdateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFormalize) -> None:
        spec = await async_client.api.v1.contracts.spec.update(
            contract_id="contract_id",
            catala_code="# Contract Formalization\n\n```catala\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n```\n",
            validate_syntax=True,
        )
        assert_matches_type(SpecUpdateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.contracts.spec.with_raw_response.update(
            contract_id="contract_id",
            catala_code="# Contract Formalization\n\n```catala\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n```\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spec = await response.parse()
        assert_matches_type(SpecUpdateResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.contracts.spec.with_streaming_response.update(
            contract_id="contract_id",
            catala_code="# Contract Formalization\n\n```catala\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n```\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spec = await response.parse()
            assert_matches_type(SpecUpdateResponse, spec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.v1.contracts.spec.with_raw_response.update(
                contract_id="",
                catala_code="# Contract Formalization\n\n```catala\ndeclaration structure Claim:\n  data amount content money\n  data date content date\n\ndeclaration scope RebateCalculation:\n  input claim content Claim\n  output rebate content money\n\nscope RebateCalculation:\n  definition rebate equals claim.amount * 0.10\n```\n",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncFormalize) -> None:
        spec = await async_client.api.v1.contracts.spec.get(
            "contract_id",
        )
        assert_matches_type(SpecGetResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.contracts.spec.with_raw_response.get(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spec = await response.parse()
        assert_matches_type(SpecGetResponse, spec, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.contracts.spec.with_streaming_response.get(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spec = await response.parse()
            assert_matches_type(SpecGetResponse, spec, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.v1.contracts.spec.with_raw_response.get(
                "",
            )
