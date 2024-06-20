class IncludeAPIRouter:
    def __new__(cls):
        from fastapi.routing import APIRouter

        from application.main.routers.anomaly_detector import (
            router as router_anomaly_detector,
        )
        from application.main.routers.health_checks import router as router_health_check

        router = APIRouter()
        router.include_router(
            router_health_check, tags=["health_check"]
        )
        router.include_router(
            router_anomaly_detector, prefix="/api/v1", tags=["Anomaly detector"]
        )
        return router
