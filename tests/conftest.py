import asyncio
from uuid import UUID
from store.core.schemas.product import ProductIn, ProductUpdate
from store.db.mongo import db_client
import pytest
from httpx import AsyncClient
from store.usecases.product import product_usecases
from tests.schemas.factories import product_data, products_data


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
        await mongo_client.get_database()[collection_name].delete_many({})


@pytest.fixture
async def client() -> AsyncClient:
    from store.main import app

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def products_url() -> str:
    return "/products/"


@pytest.fixture
def product_id() -> UUID:
    return UUID("32764181-35b4-4a56-81ae-50c445055c6b")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)


@pytest.fixture
def products_in():
    return [ProductIn(**product) for product in products_data()]


@pytest.fixture
def product_up(product_id):
    return ProductUpdate(**product_data(), id=product_id)


@pytest.fixture
async def product_insert(product_in):
    return await product_usecases.create(body=product_in)


@pytest.fixture
async def products_insert(products_in):
    return [
        await product_usecases.create(body=product_in) for product_in in products_in
    ]
