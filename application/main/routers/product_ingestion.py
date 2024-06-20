# app/api/routers/anomaly_detector.py
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException
from loguru import logger

from application.main.containers import Container
from application.main.domain.entities.product import ProductStatsList
from application.main.infrastructure.schemas.product import (
    IngestProductStatsListResponse,
)
from application.main.services.product_ingestion_service import ProductIngestionService

router = APIRouter(prefix="/load")


@router.post("/item_stats", response_model=IngestProductStatsListResponse)
@inject
async def ingest_product(
    product_list: ProductStatsList,
    service: ProductIngestionService = Depends(Provide[Container.ingestion_service]),
):
    try:
        logger.info(f"Ingesting: {product_list.length()} items.")
        result = await service.ingest_batch(product_list)
        return IngestProductStatsListResponse(ingested_items=result, code=200)

    except Exception as ex:
        if hasattr(ex, "status_code") and hasattr(ex, "message"):
            logger.error(str(ex))
            raise HTTPException(status_code=ex.status_code, detail=ex.message)
        else:
            logger.error(str(ex))
            raise HTTPException(status_code=500, detail=str(ex))
