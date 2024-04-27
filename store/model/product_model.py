from store.core.schemas.product import ProductIn
from store.model.base import CreateBaseModel


class ProductModel(ProductIn, CreateBaseModel):
    ...
