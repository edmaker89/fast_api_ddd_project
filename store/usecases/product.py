from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from store.core.schemas.product import ProductIn
from store.db.mongo import db_client


class ProductUsecases:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn):
        await self.collection.insert_one(body.model_dump())


product_usecases = ProductUsecases()
