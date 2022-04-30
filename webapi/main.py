import logging
import uvicorn

from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics
from core.config import settings
from webapi.api.v1.api import api_router


logging.basicConfig(
    level=logging.getLevelName(settings.logging.level), format=settings.logging.format
)

logger = logging.getLogger("uvicorn.error")

app = FastAPI(title="Metrics Collector")
app.include_router(api_router, prefix="/v1")
app.add_middleware(PrometheusMiddleware, app_name="python_webapi", group_paths=True)
app.add_route("/metrics", handle_metrics)

if __name__ == "__main__":
    logger.info("Starting server")
    logger.warning("This is debug server")
    logger.warning("To start server use command: uvicorn main:app --reload")
    uvicorn.run(app, port=settings.web.port, host=settings.web.host)
