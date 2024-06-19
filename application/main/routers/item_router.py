# app/api/routers/item_router.py
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from loguru import logger

from application.main.containers import Container
from application.main.infrastructure.schemas.product import (
    InferenceOutput,
    ProductInput,
)
from application.main.services.anomaly_se import AnomalyDetectorService

router = APIRouter(prefix="/anomaly-price-detector-v2")


@router.post("/run", response_model=InferenceOutput)
@inject
async def anomaly_price_detector(
    product_info: ProductInput,
    service: AnomalyDetectorService = Depends(
        Provide[Container.anomaly_detector_service]
    ),
):
    item_id = product_info.item_id
    price = product_info.price

    logger.debug(f"detecting anomaly price for item: {item_id} with price: {price}")

    anomaly_response = await service.classify(item_id=item_id, price=price)

    resp = InferenceOutput(
        item_id=item_id, price=price, anomaly=anomaly_response, code=200
    )
    return resp
