# app/services/anomaly_detector_service.py
from application.main.infrastructure.repositories.anomaly_detector import MLModel
import numpy as np

class AnomalyDetectorService:
    def __init__(self, model: MLModel):
        self.model = model

    def classify(self, price: int) -> str:
        return self.model.inference(np.array([price]).reshape(1, -1))