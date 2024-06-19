import joblib
import numpy as np

from application.main.config import settings


class AnomalyDetector:
    def __init__(self):
        self.detector = joblib.load(
            open(settings.APP_CONFIG.ANOMALY_DETECTOR_MODEL, "rb")
        )

    def anomaly_detector_inf(self, price: int) -> int:
        return self.detector.predict(price)


class AnomalyDetectorService:
    def __init__(self):
        self.anomaly_detector = AnomalyDetector()

    def classify(self, price: int) -> str:

        return self.anomaly_detector.anomaly_detector_inf(
            np.array([price]).reshape(1, -1)
        )
