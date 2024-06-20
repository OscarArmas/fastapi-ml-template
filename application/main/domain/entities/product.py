from typing import Any, Dict, List

from pydantic import BaseModel, Field

from application.main.domain.exceptions import PriceIsLessThanOrEqualToZero


class ProductInput(BaseModel):
    item_id: str
    price: float


class ProductStats(BaseModel):
    _id: str
    historical_prices: List[float]
    lower_bound: float
    upper_bound: float
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ProductStatsList(BaseModel):
    items: List[ProductStats]

    def length(self) -> int:
        return len(self.items)

    def to_dict_list(self) -> List[Dict[str, Any]]:
        return [item.model_dump() for item in self.items]
