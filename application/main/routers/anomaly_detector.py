from fastapi.routing import APIRouter
from loguru import logger

from application.main.services.anomaly_detector_service import AnomalyDetectorService
from application.main.infrastructure.schemas.product import ProductInput, InferenceOutput

anomaly_detector_service = AnomalyDetectorService()
router = APIRouter(prefix='/anomaly-price-detector')


@router.post("/run", response_model = InferenceOutput)
async def anonamy_price_detector(product_info: ProductInput):
    name, price  = product_info.__dict__.values()

    logger.debug(f"detecting anomaly price for product: {name} with price: {price}")
    anomaly_response = anomaly_detector_service.classify(price)
    resp = InferenceOutput(id=100, anomaly=anomaly_response[0])
    return resp
