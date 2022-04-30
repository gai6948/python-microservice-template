from typing import Dict
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/fib", tags=["fib"])
async def get_fib(n: int = 0) -> Dict:
    if n > 250:
        raise HTTPException(
            status_code=400,
            detail="Max fibonacci number supported is 250"
        )
    return {
        "value": generate_fibonacci(n),
    }


def generate_fibonacci(n: int):
    if n <= 1:
        return 1
    return generate_fibonacci(n-2) + generate_fibonacci(n-1)
