# app/services/anomaly_detector_service.py
from application.main.domain.entities.product import ProductStatsList
from application.main.infrastructure.repositories.db.base_db import DataBase


class ProductIngestionService:
    def __init__(self, db: DataBase):
        self.db = db

    async def ingest_batch(self, product_list: ProductStatsList) -> bool:
        return await self.db.insert_multiple_db_record(product_list.to_dict_list())
