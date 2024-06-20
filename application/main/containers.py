# app/containers.py
from dependency_injector import containers, providers

from application.main.config import settings
from application.main.infrastructure.repositories.cache.redis_cache import RedisCache
from application.main.infrastructure.repositories.db.mongo_db import Mongodb
from application.main.infrastructure.repositories.models.anomaly_model import (
    AnomalyModel,
)

from .services.anomaly_detector_service import AnomalyDetectorService


class Container(containers.DeclarativeContainer):
    # Instances
    redis_instance = providers.Singleton(RedisCache, redis_url=settings.REDIS_URL)

    mongo_instance = providers.Singleton(
        Mongodb,
        user=settings.MONGO_USER,
        psw=settings.MONGO_PASS,
        host=settings.MONGO_HOST,
        port=settings.MONGO_PORT,
        db_name=settings.MONGO_DB,
        collection_name=settings.MONGO_COLLECTION,
    )

    # Models
    ml_model = providers.Singleton(
        AnomalyModel, model_path=settings.APP_CONFIG.ANOMALY_DETECTOR_MODEL
    )

    # Services
    anomaly_detector_service = providers.Factory(
        AnomalyDetectorService, model=ml_model, cache=redis_instance, db=mongo_instance
    )
