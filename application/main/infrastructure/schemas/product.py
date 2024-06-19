from typing import Optional

from pydantic import BaseModel


class ProductInput(BaseModel):
    item_id: str
    price: float


class InferenceOutput(BaseModel):
    item_id: str
    price: float
    anomaly: bool
    metadata: Optional[str] = {}
    code: int
