# app/api/routers/item_router.py
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from application.main.services.anomaly_se import AnomalyDetectorService
from application.main.containers import Container
from application.main.infrastructure.schemas.product import ProductInput, InferenceOutput
from loguru import logger



router = APIRouter(prefix='/anomaly-price-detector-v2')

@router.post("/run", response_model=InferenceOutput)
@inject
async def anomaly_price_detector(
    product_info: ProductInput,
    service: AnomalyDetectorService = Depends(Provide[Container.anomaly_detector_service])
):
    name = product_info.name
    price = product_info.price
    
    logger.debug(f"detecting anomaly price for product: {name} with price: {price}")
    
    anomaly_response = service.classify(price)
    
    resp = InferenceOutput(id=100, anomaly=anomaly_response[0])
    return resp