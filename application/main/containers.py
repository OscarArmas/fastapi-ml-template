# app/containers.py
from dependency_injector import containers, providers
from .services.anomaly_se import AnomalyDetectorService
from application.main.infrastructure.repositories.anomaly_detector import AnomalyDetector
from application.main.config import settings

class Container(containers.DeclarativeContainer):

    #models
    ml_model = providers.Singleton(
        AnomalyDetector,
        model_path=settings.APP_CONFIG.ANOMALY_DETECTOR_MODEL
    )

    #services
    anomaly_detector_service = providers.Factory(
        AnomalyDetectorService,
        model=ml_model
    )
