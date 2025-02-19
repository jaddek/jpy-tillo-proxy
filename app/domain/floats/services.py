import logging
from typing import Optional

from httpx import Response
from jpy_tillo_sdk.domain.float.endpoints import CheckFloatsEndpoint
from jpy_tillo_sdk.domain.float.factory import create_check_floats_query
from jpy_tillo_sdk.domain.float.services import FloatService
from jpy_tillo_sdk.enums import Currency
from tillo.clients import tillo_client_async

logger = logging.getLogger(__name__)

async def get_float_by_currency_async(currency: Optional[Currency]) -> Response:
    response = await FloatService.check_floats_async(
        tillo_client_async,
        create_check_floats_query(currency)
    )

    return response


async def get_floats_async() -> Response:
    response = await FloatService.check_floats_async(
        tillo_client_async,
        CheckFloatsEndpoint.QueryParams()
    )

    return response

