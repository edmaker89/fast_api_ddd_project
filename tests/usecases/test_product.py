from typing import List
from uuid import UUID

import pytest
from store.core.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecases
from store.core.execeptions import NotFoundException


async def test_usecases_should_return_sucess(product_in):
    result = await product_usecases.create(body=product_in)

    # assert result is None
    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro Max"


async def test_usecases_get_should_return_sucess(product_id):
    result = await product_usecases.get(id=product_id)

    # assert result is None
    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro Max"


async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecases.get(id=UUID("1fed55bf-c1ac-4446-8c88-92b13a01ae6c"))

    assert (
        err.value.message
        == "Product not found with filter: 1fed55bf-c1ac-4446-8c88-92b13a01ae6c"
    )


async def test_usecases_query_should_return_sucess():
    result = await product_usecases.query()

    # assert result is None
    assert isinstance(result, List)


async def test_usecases_update_should_return_sucess(product_id, product_up):
    product_up.price = 7.500

    result = await product_usecases.update(id=product_id, body=product_up)

    # assert result is None
    assert isinstance(result, ProductUpdateOut)
