from pydantic import ValidationError
import pytest
from store.core.schemas.product import ProductIn
from tests.schemas.factories import product_data


def test_schemas_return_success():
    product = ProductIn.model_validate(product_data())

    assert product.name == "Iphone 14 pro Max"


def test_schemas_return_raise():
    data = product_data()
    data.pop("status", None)
    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert "missing" in str(err.value) and "status" in str(err.value)
