from abc import ABC, abstractmethod
from typing import Any


class MLModel(ABC):
    @abstractmethod
    def load_model(self, model_path: str, *params, **kwargs) -> None:
        pass

    @abstractmethod
    def inference(self, *params, **kwargs) -> Any:
        pass
