# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from formalize import Formalize, AsyncFormalize
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Formalize) -> None:
        dataset = client.api.contracts.datasets.create(
            contract_id="contract_id",
            name="name",
            file=b"Example data",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Formalize) -> None:
        dataset = client.api.contracts.datasets.create(
            contract_id="contract_id",
            name="name",
            file=b"Example data",
            description="description",
            is_primary=True,
            target_scope="target_scope",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Formalize) -> None:
        response = client.api.contracts.datasets.with_raw_response.create(
            contract_id="contract_id",
            name="name",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Formalize) -> None:
        with client.api.contracts.datasets.with_streaming_response.create(
            contract_id="contract_id",
            name="name",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.create(
                contract_id="",
                name="name",
                file=b"Example data",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Formalize) -> None:
        dataset = client.api.contracts.datasets.retrieve(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Formalize) -> None:
        response = client.api.contracts.datasets.with_raw_response.retrieve(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Formalize) -> None:
        with client.api.contracts.datasets.with_streaming_response.retrieve(
            dataset_id="dataset_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.retrieve(
                dataset_id="dataset_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.retrieve(
                dataset_id="",
                contract_id="contract_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Formalize) -> None:
        dataset = client.api.contracts.datasets.update(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Formalize) -> None:
        dataset = client.api.contracts.datasets.update(
            dataset_id="dataset_id",
            contract_id="contract_id",
            description="description",
            is_primary=True,
            name="name",
            target_scope="target_scope",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Formalize) -> None:
        response = client.api.contracts.datasets.with_raw_response.update(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Formalize) -> None:
        with client.api.contracts.datasets.with_streaming_response.update(
            dataset_id="dataset_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.update(
                dataset_id="dataset_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.update(
                dataset_id="",
                contract_id="contract_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Formalize) -> None:
        dataset = client.api.contracts.datasets.list(
            "contract_id",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Formalize) -> None:
        response = client.api.contracts.datasets.with_raw_response.list(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Formalize) -> None:
        with client.api.contracts.datasets.with_streaming_response.list(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Formalize) -> None:
        dataset = client.api.contracts.datasets.delete(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Formalize) -> None:
        response = client.api.contracts.datasets.with_raw_response.delete(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Formalize) -> None:
        with client.api.contracts.datasets.with_streaming_response.delete(
            dataset_id="dataset_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.delete(
                dataset_id="dataset_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.delete(
                dataset_id="",
                contract_id="contract_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_columns(self, client: Formalize) -> None:
        dataset = client.api.contracts.datasets.generate_columns(
            dataset_id="dataset_id",
            contract_id="contract_id",
            fields=["string"],
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_columns(self, client: Formalize) -> None:
        response = client.api.contracts.datasets.with_raw_response.generate_columns(
            dataset_id="dataset_id",
            contract_id="contract_id",
            fields=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_columns(self, client: Formalize) -> None:
        with client.api.contracts.datasets.with_streaming_response.generate_columns(
            dataset_id="dataset_id",
            contract_id="contract_id",
            fields=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_generate_columns(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.generate_columns(
                dataset_id="dataset_id",
                contract_id="",
                fields=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.generate_columns(
                dataset_id="",
                contract_id="contract_id",
                fields=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_download(self, client: Formalize) -> None:
        dataset = client.api.contracts.datasets.retrieve_download(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_download(self, client: Formalize) -> None:
        response = client.api.contracts.datasets.with_raw_response.retrieve_download(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_download(self, client: Formalize) -> None:
        with client.api.contracts.datasets.with_streaming_response.retrieve_download(
            dataset_id="dataset_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_download(self, client: Formalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.retrieve_download(
                dataset_id="dataset_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.api.contracts.datasets.with_raw_response.retrieve_download(
                dataset_id="",
                contract_id="contract_id",
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFormalize) -> None:
        dataset = await async_client.api.contracts.datasets.create(
            contract_id="contract_id",
            name="name",
            file=b"Example data",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFormalize) -> None:
        dataset = await async_client.api.contracts.datasets.create(
            contract_id="contract_id",
            name="name",
            file=b"Example data",
            description="description",
            is_primary=True,
            target_scope="target_scope",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.datasets.with_raw_response.create(
            contract_id="contract_id",
            name="name",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.datasets.with_streaming_response.create(
            contract_id="contract_id",
            name="name",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.create(
                contract_id="",
                name="name",
                file=b"Example data",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFormalize) -> None:
        dataset = await async_client.api.contracts.datasets.retrieve(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.datasets.with_raw_response.retrieve(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.datasets.with_streaming_response.retrieve(
            dataset_id="dataset_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.retrieve(
                dataset_id="dataset_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.retrieve(
                dataset_id="",
                contract_id="contract_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFormalize) -> None:
        dataset = await async_client.api.contracts.datasets.update(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFormalize) -> None:
        dataset = await async_client.api.contracts.datasets.update(
            dataset_id="dataset_id",
            contract_id="contract_id",
            description="description",
            is_primary=True,
            name="name",
            target_scope="target_scope",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.datasets.with_raw_response.update(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.datasets.with_streaming_response.update(
            dataset_id="dataset_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.update(
                dataset_id="dataset_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.update(
                dataset_id="",
                contract_id="contract_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFormalize) -> None:
        dataset = await async_client.api.contracts.datasets.list(
            "contract_id",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.datasets.with_raw_response.list(
            "contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.datasets.with_streaming_response.list(
            "contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncFormalize) -> None:
        dataset = await async_client.api.contracts.datasets.delete(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.datasets.with_raw_response.delete(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.datasets.with_streaming_response.delete(
            dataset_id="dataset_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.delete(
                dataset_id="dataset_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.delete(
                dataset_id="",
                contract_id="contract_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_columns(self, async_client: AsyncFormalize) -> None:
        dataset = await async_client.api.contracts.datasets.generate_columns(
            dataset_id="dataset_id",
            contract_id="contract_id",
            fields=["string"],
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_columns(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.datasets.with_raw_response.generate_columns(
            dataset_id="dataset_id",
            contract_id="contract_id",
            fields=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_columns(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.datasets.with_streaming_response.generate_columns(
            dataset_id="dataset_id",
            contract_id="contract_id",
            fields=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_generate_columns(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.generate_columns(
                dataset_id="dataset_id",
                contract_id="",
                fields=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.generate_columns(
                dataset_id="",
                contract_id="contract_id",
                fields=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_download(self, async_client: AsyncFormalize) -> None:
        dataset = await async_client.api.contracts.datasets.retrieve_download(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_download(self, async_client: AsyncFormalize) -> None:
        response = await async_client.api.contracts.datasets.with_raw_response.retrieve_download(
            dataset_id="dataset_id",
            contract_id="contract_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_download(self, async_client: AsyncFormalize) -> None:
        async with async_client.api.contracts.datasets.with_streaming_response.retrieve_download(
            dataset_id="dataset_id",
            contract_id="contract_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_download(self, async_client: AsyncFormalize) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.retrieve_download(
                dataset_id="dataset_id",
                contract_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.api.contracts.datasets.with_raw_response.retrieve_download(
                dataset_id="",
                contract_id="contract_id",
            )
