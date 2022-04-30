from fastapi import APIRouter

from webapi.api.v1.endpoints import fib, pairs

api_router = APIRouter()
api_router.include_router(pairs.router, tags=["pairs"])
api_router.include_router(fib.router, tags=["fib"])
