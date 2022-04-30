import random
from typing import Dict
from fastapi import APIRouter
from core import metrics

router = APIRouter()


@router.get("/pairs", tags=["pairs"])
async def get_pairs() -> Dict:
    metrics.GET_PAIRS_COUNT.inc()
    return {
        "USDRUB": round(random.random() * 100, 2),
        "EURRUB": round(random.random() * 100, 2)
    }
