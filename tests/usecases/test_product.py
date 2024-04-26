from store.usecases.product import product_usecases


async def test_usecases_should_return_sucess(product_in):
    result = product_usecases.create(body=product_in)

    assert result is None
    # assert isinstance(result, ProductOut)
