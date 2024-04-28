from datetime import datetime
from typing import List, Optional
from uuid import UUID
from bson import Decimal128
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from store.core.schemas.product import (
    ProductIn,
    ProductOut,
    ProductUpdate,
    ProductUpdateOut,
)
from store.db.mongo import db_client
from store.core.execeptions import NotFoundException
import pymongo

from store.model.product_model import ProductModel


class ProductUsecases:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())
        product = ProductOut(**product_model.model_dump())
        await self.collection.insert_one(product_model.model_dump())

        return product

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        return ProductOut(**result)

    async def query(
        self, min_price: Optional[float] = None, max_price: Optional[float] = None
    ) -> List[ProductOut]:
        filter_query = {}
        if min_price is not None:
            filter_query["price"] = {"$gte": Decimal128(str(min_price))}
        if max_price is not None:
            if "price" in filter_query:
                filter_query["price"]["$lte"] = Decimal128(str(max_price))
            else:
                filter_query["price"] = {"$lte": Decimal128(str(max_price))}

        return [ProductOut(**item) async for item in self.collection.find(filter_query)]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        update_data = body.model_dump(exclude_none=True)
        update_data["updated_at"] = datetime.now()
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": update_data},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        result = await self.collection.delete_one({"id": id})
        return result.deleted_count > 0


product_usecases = ProductUsecases()
