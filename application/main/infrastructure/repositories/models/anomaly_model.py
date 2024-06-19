# app/repositories/anomaly_detector.py
from dataclasses import dataclass, field

import joblib

from .base_model import MLModel


@dataclass
class AnomalyModel(MLModel):
    model_path: str
    model: any = field(init=False, default=None)

    def __post_init__(self):
        self.load_model(self.model_path)

    def load_model(self, model_path: str) -> None:
        self.model = joblib.load(model_path)

    def inference(self, price: float) -> bool:
        if not self.model:
            raise ValueError("Model not loaded")
        return self.model.predict(price)
