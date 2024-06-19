# app/services/anomaly_detector_service.py
from application.main.infrastructure.repositories.cache.base_cache import BaseCache
from application.main.infrastructure.repositories.db.base_db import DataBaseOperations
from application.main.infrastructure.repositories.models.anomaly_model import MLModel


class AnomalyDetectorService:
    def __init__(self, model: MLModel, cache: BaseCache, db: DataBaseOperations):
        self.model = model
        self.cache = cache
        self.db = db

    async def classify(self, item_id: str, price: int) -> bool:

        key_id = f"{item_id}_{price}"

        result = await self.cache.get(key_id)
        if result is not None:
            return result

        result = await self.detect_anomaly(item_id, price)

        await self.cache.set(key_id, str(result))
        return result

    async def get_stats_by_items(self, item_id: str):

        return await self.db.fetch_single_db_record(item_id)

    async def detect_anomaly(self, item_id: str, price: float) -> bool:

        stats = await self.get_stats_by_items(item_id)
        lower_bound = stats["lower_bound"]
        upper_bound = stats["upper_bound"]

        return (price < lower_bound) | (price > upper_bound)
