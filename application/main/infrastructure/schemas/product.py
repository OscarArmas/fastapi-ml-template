from typing import Any, Dict

from pydantic import BaseModel, Field


class InferenceResponse(BaseModel):
    item_id: str
    price: float
    anomaly: bool
    metadata: Dict[str, Any] = Field(default_factory=dict)


class IngestProductStatsListResponse(BaseModel):
    ingested_items: int
    code: int
