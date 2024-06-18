# app/repositories/anomaly_detector.py
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Any
import joblib

class MLModel(ABC):
    @abstractmethod
    def load_model(self, model_path: str, *params, **kwargs) -> None:
        pass

    @abstractmethod
    def inference(self, *params, **kwargs) -> Any:
        pass

@dataclass
class AnomalyDetector(MLModel):
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
