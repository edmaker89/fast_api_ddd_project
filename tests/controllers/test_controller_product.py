from typing import List

import pytest
from tests.schemas.factories import product_data
from fastapi import status


async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())

    content = response.json()
    del content["created_at"]
    del content["updated_at"]
    del content["id"]
    assert response.status_code == status.HTTP_201_CREATED
    assert content == {
        "name": "Iphone 14 pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_controller_get_should_return_success(
    client, products_url, product_insert
):
    response = await client.get(f"{products_url}{product_insert.id}")

    content = response.json()

    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert {
        "id": str(product_insert.id),
        "name": "Iphone 14 pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }
    assert response.status_code == status.HTTP_200_OK


async def test_controller_get_should_return_not_found(client, products_url):
    response = await client.get(f"{products_url}29388d0b-7f9a-4d83-9056-ff58417420e9")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert (
        response.json()["detail"]
        == "Product not found with filter: 29388d0b-7f9a-4d83-9056-ff58417420e9"
    )


@pytest.mark.usefixtures("products_insert")
async def test_controller_query_should_return_success(
    client, products_url, products_insert
):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1


@pytest.mark.usefixtures("products_insert")
async def test_controller_query_with_price_range_should_return_success(
    client, products_url, products_insert
):
    min_price = "1100.00"
    max_price = "2000.00"
    response = await client.get(
        f"{products_url}?min_price={min_price}&max_price={max_price}"
    )

    assert response.status_code == status.HTTP_200_OK
    results = response.json()
    assert isinstance(results, List)
    assert len(results) > 1

    for product in results:
        assert min_price <= product["price"] <= max_price


@pytest.mark.usefixtures("products_insert")
async def test_controller_query_with_invalid_price_range_return_exception(
    client, products_url, products_insert
):
    min_price = "2500.00"
    max_price = "1500.00"
    response = await client.get(
        f"{products_url}?min_price={min_price}&max_price={max_price}"
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    error_message = response.json().get("detail")
    assert "Minimum price cannot be greater than maximum price" in error_message


async def test_controller_patch_should_return_success(
    client, products_url, product_insert
):
    response = await client.patch(
        f"{products_url}{product_insert.id}", json={"quantity": 40}
    )

    content = response.json()

    assert content["created_at"] != content["updated_at"]

    del content["created_at"]
    del content["updated_at"]

    assert {
        "id": str(product_insert.id),
        "name": "Iphone 14 pro Max",
        "quantity": 40,
        "price": "8.500",
        "status": True,
    }
    assert response.status_code == status.HTTP_200_OK


async def test_controller_delete_should_return_no_content(
    client, products_url, product_insert
):
    response = await client.delete(f"{products_url}{product_insert.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_should_return_not_found(client, products_url):
    response = await client.delete(
        f"{products_url}29388d0b-7f9a-4d83-9056-ff58417420e9"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert (
        response.json()["detail"]
        == "Product not found with filter: 29388d0b-7f9a-4d83-9056-ff58417420e9"
    )
