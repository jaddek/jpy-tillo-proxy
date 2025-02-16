from typing import Annotated

from app.domain.floats.body_requests import TransferRequestBody
from jpy_tillo_sdk.enums import Currency
from fastapi import APIRouter, Query, Path, Body
from app.tillo.services import get_float_by_currency, get_floats

router = APIRouter(prefix="/floats", tags=["Floats"])


@router.get("")
async def floats():
    response = await get_floats()

    return response.json()


@router.get("/{currency}")
async def floats(
        currency: Annotated[
            Currency,
            Path(
                title="FIAT Currency",
                description="Currency name, for example 'EUR'",
            )
        ]):
    response = await get_float_by_currency(currency)

    return response.json()


@router.post("/transfer")
async def transfer_request(
        body: Annotated[
            TransferRequestBody,
            Body(
                title="Payment Transfer Details",
                description="Contains the required information for initiating a payment transfer, including amount, currency, and recipient."
            )
        ]
):
    return {"message": "payment transfer", "body": body}
