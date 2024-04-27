import asyncio
from uuid import UUID
from store.core.schemas.product import ProductIn, ProductUpdate
from store.db.mongo import db_client
import pytest

from tests.schemas.factories import product_data


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collections_name = await mongo_client.get_database().list_collection_names()
    for collection_name in collections_name:
        if collection_name.startswith("system"):
            continue
        # await mongo_client.get_database()[collection_name].delete_many({})


@pytest.fixture
def product_id() -> UUID:
    return UUID("32764181-35b4-4a56-81ae-50c445055c6b")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)


@pytest.fixture
def product_up(product_id):
    return ProductUpdate(**product_data(), id=product_id)
