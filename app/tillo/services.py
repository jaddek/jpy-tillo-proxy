import logging
from typing import Optional

from httpx import Response
from jpy_tillo_sdk.domain.brand.factory import create_brands_query_params, create_brand_template_list_query_params, \
    create_brand_template_query_params
from jpy_tillo_sdk.domain.brand.services import BrandService, TemplateService
from jpy_tillo_sdk.domain.float.endpoints import CheckFloatsEndpoint
from jpy_tillo_sdk.domain.float.factory import create_check_floats_query
from jpy_tillo_sdk.domain.float.services import FloatService
from jpy_tillo_sdk.enums import Currency

from .clients import tillo_client_async

logger = logging.getLogger(__name__)


async def get_brands(detail: bool = False) -> Response:
    logger.info("Cache?")

    response = await BrandService.get_available_brands_async(
        tillo_client_async,
        query_params=create_brands_query_params(
            detail=detail
        )
    )

    return response


async def get_brand_templates(brand: str) -> Response:
    response = await TemplateService.get_brand_templates_async(
        tillo_client_async,
        query_params=create_brand_template_list_query_params(
            brand=brand
        )
    )

    return response


async def get_brand_template(brand: str, template: str) -> Response:
    response = await TemplateService.download_brand_template_async(
        tillo_client_async,
        query_params=create_brand_template_query_params(
            brand=brand,
            template=template,
        )
    )

    return response


async def get_float_by_currency(currency: Optional[Currency]) -> Response:
    response = await FloatService.check_floats_async(
        tillo_client_async,
        create_check_floats_query(currency)
    )

    return response


async def get_floats() -> Response:
    response = await FloatService.check_floats_async(
        tillo_client_async,
        CheckFloatsEndpoint.QueryParams()
    )

    return response


async def read_brand_template(response: Response):
    async for chunk in response.aiter_bytes(8192):
        yield chunk
