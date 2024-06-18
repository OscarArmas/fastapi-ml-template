from pydantic import BaseModel


class ProductInput(BaseModel):
    name: str
    price: float

class InferenceOutput(BaseModel):
    id: int
    anomaly: int


