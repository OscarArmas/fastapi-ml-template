from typing import Optional

from pydantic import BaseModel
from typing import Dict, Any

class ProductInput(BaseModel):
    item_id: str
    price: float


class InferenceOutput(BaseModel):
    item_id: str
    price: float
    anomaly: bool
    metadata: Dict[Any, Any] = {}
