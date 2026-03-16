# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type
from formalize.types.api.v1.contracts import (
    AuditBatchResponse,
    AuditCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Formalize) -> None:
        audit = client.api.v1.contracts.audit.create(
            contract_id="contract_id",
            inputs={
                "claim": "bar",
                "contract_terms": "bar",
            },
        )
        assert_matches_type(AuditCreateResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Formalize) -> None:
        audit = client.api.v1.contracts.audit.create(
            contract_id="contract_id",
            inputs={
                "claim": "bar",
                "contract_terms": "bar",
            },
            scope_name="RebateCalculation",
        )
        assert_matches_type(AuditCreateResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Formalize) -> None:
        response = client.api.v1.contracts.audit.with_raw_response.create(
            contract_id="contract_id",
            inputs={
                "claim": "bar",
                "contract_terms": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = response.parse()
        assert_matches_type(AuditCreateResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Formalize) -> None:
        with client.api.v1.contracts.audit.with_streaming_response.create(
            contract_id="contract_id",
            inputs={
                "claim": "bar",
                "contract_terms": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = response.parse()
            assert_matches_type(AuditCreateResponse, audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.v1.contracts.audit.with_raw_response.create(
                contract_id="",
                inputs={
                    "claim": "bar",
                    "contract_terms": "bar",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch(self, client: Formalize) -> None:
        audit = client.api.v1.contracts.audit.batch(
            contract_id="contract_id",
            scenarios=[{"claim": "bar"}, {"claim": "bar"}],
        )
        assert_matches_type(AuditBatchResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_with_all_params(self, client: Formalize) -> None:
        audit = client.api.v1.contracts.audit.batch(
            contract_id="contract_id",
            scenarios=[{"claim": "bar"}, {"claim": "bar"}],
            scope_name="RebateCalculation",
        )
        assert_matches_type(AuditBatchResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch(self, client: Formalize) -> None:
        response = client.api.v1.contracts.audit.with_raw_response.batch(
            contract_id="contract_id",
            scenarios=[{"claim": "bar"}, {"claim": "bar"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = response.parse()
        assert_matches_type(AuditBatchResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch(self, client: Formalize) -> None:
        with client.api.v1.contracts.audit.with_streaming_response.batch(
            contract_id="contract_id",
            scenarios=[{"claim": "bar"}, {"claim": "bar"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = response.parse()
            assert_matches_type(AuditBatchResponse, audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_batch(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.v1.contracts.audit.with_raw_response.batch(
                contract_id="",
                scenarios=[{"claim": "bar"}, {"claim": "bar"}],
            )


class TestAsyncAudit:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFormalize) -> None:
        audit = await async_client.api.v1.contracts.audit.create(
            contract_id="contract_id",
            inputs={
                "claim": "bar",
                "contract_terms": "bar",
            },
        )
        assert_matches_type(AuditCreateResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFormalize) -> None:
        audit = await async_client.api.v1.contracts.audit.create(
            contract_id="contract_id",
            inputs={
                "claim": "bar",
                "contract_terms": "bar",
            },
            scope_name="RebateCalculation",
        )
        assert_matches_type(AuditCreateResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.contracts.audit.with_raw_response.create(
            contract_id="contract_id",
            inputs={
                "claim": "bar",
                "contract_terms": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = await response.parse()
        assert_matches_type(AuditCreateResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.contracts.audit.with_streaming_response.create(
            contract_id="contract_id",
            inputs={
                "claim": "bar",
                "contract_terms": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = await response.parse()
            assert_matches_type(AuditCreateResponse, audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.v1.contracts.audit.with_raw_response.create(
                contract_id="",
                inputs={
                    "claim": "bar",
                    "contract_terms": "bar",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch(self, async_client: AsyncFormalize) -> None:
        audit = await async_client.api.v1.contracts.audit.batch(
            contract_id="contract_id",
            scenarios=[{"claim": "bar"}, {"claim": "bar"}],
        )
        assert_matches_type(AuditBatchResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_with_all_params(self, async_client: AsyncFormalize) -> None:
        audit = await async_client.api.v1.contracts.audit.batch(
            contract_id="contract_id",
            scenarios=[{"claim": "bar"}, {"claim": "bar"}],
            scope_name="RebateCalculation",
        )
        assert_matches_type(AuditBatchResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.v1.contracts.audit.with_raw_response.batch(
            contract_id="contract_id",
            scenarios=[{"claim": "bar"}, {"claim": "bar"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = await response.parse()
        assert_matches_type(AuditBatchResponse, audit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.v1.contracts.audit.with_streaming_response.batch(
            contract_id="contract_id",
            scenarios=[{"claim": "bar"}, {"claim": "bar"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = await response.parse()
            assert_matches_type(AuditBatchResponse, audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_batch(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.v1.contracts.audit.with_raw_response.batch(
                contract_id="",
                scenarios=[{"claim": "bar"}, {"claim": "bar"}],
            )
