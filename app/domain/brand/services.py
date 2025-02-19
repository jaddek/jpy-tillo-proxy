import logging

from httpx import Response
from jpy_tillo_sdk.domain.brand.factory import create_brands_query_params, create_brand_template_list_query_params, \
    create_brand_template_query_params
from jpy_tillo_sdk.domain.brand.services import BrandService, TemplateService
from tillo.clients import tillo_client_async

logger = logging.getLogger(__name__)


async def get_brands(detail: bool = False) -> Response:
    response = await BrandService.get_available_brands_async(
        tillo_client_async,
        query_params=create_brands_query_params(
            detail=detail
        )
    )

    return response


async def get_brand_templates_async(brand: str) -> Response:
    response = await TemplateService.get_brand_templates_async(
        tillo_client_async,
        query_params=create_brand_template_list_query_params(
            brand=brand
        )
    )

    return response


async def get_brand_template_async(brand: str, template: str) -> Response:
    response = await TemplateService.download_brand_template_async(
        tillo_client_async,
        query_params=create_brand_template_query_params(
            brand=brand,
            template=template,
        )
    )

    return response


async def read_brand_template_async(response: Response):
    async for chunk in response.aiter_bytes(8192):
        yield chunk
