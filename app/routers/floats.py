from fastapi import APIRouter
from jpy_tillo_sdk.enums import Currency

from app.tillo.services import get_float_by_currency, get_floats

router = APIRouter(prefix="/floats", tags=["Floats"])


@router.get("")
async def floats():
    response = await get_floats()

    return response.json()


@router.get("/{currency}")
async def floats(currency: Currency):
    response = await get_float_by_currency(currency)

    return response.json()


@router.get("/transfer/request")
async def transfer_request():
    return {"message": "payment transfer"}
