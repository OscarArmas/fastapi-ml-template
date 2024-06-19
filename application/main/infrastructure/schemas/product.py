from pydantic import BaseModel
from typing import Optional

class ProductInput(BaseModel):
    item_id: str
    price: float

class InferenceOutput(BaseModel):
    item_id: str
    price: float
    anomaly: bool
    metadata: Optional[str] = {}
    code: int

