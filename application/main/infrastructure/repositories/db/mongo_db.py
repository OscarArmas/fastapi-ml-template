from abc import ABC

import motor.motor_asyncio
from .base_db import DataBaseOperations

class Mongodb(DataBaseOperations, ABC):

    def __init__(self, user, psw, host, port, db_name, collection_name):
        super().__init__()
        self.connection_uri = f"mongodb://{user}:{psw}@{host}:{port}/{db_name}?authSource=admin&retryWrites=true&w=majority"
        self.collection_name = collection_name
        self.db_name = db_name
        self.client = None
        self.collection = None

    async def connect(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.connection_uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    async def fetch_single_db_record(self, unique_id: str):
        if self.collection is None:
            await self.connect()
        document = await self.collection.find_one({"ITEM_ID": unique_id})
        return document
