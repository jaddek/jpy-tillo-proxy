from functools import lru_cache

from httpx import Response
from jpy_tillo_sdk.domain.brand.factory import create_brands_query_params, create_brand_template_list_query_params, \
    create_brand_template_query_params

from .clients import tillo_client
from jpy_tillo_sdk.domain.brand.services import BrandService, TemplateService
import logging

logger = logging.getLogger(__name__)


@lru_cache(maxsize=100)
def get_brands(detail: bool = False) -> Response:
    logger.info("Cache?")

    return BrandService.get_available_brands(
        tillo_client,
        query_params=create_brands_query_params(
            detail=detail
        )
        .get_not_empty_values()
    )


@lru_cache(maxsize=100)
def get_brand_templates(brand: str) -> Response:
    return TemplateService.get_brand_templates(
        tillo_client,
        query_params=create_brand_template_list_query_params(
            brand=brand
        )
        .get_not_empty_values()
    )


@lru_cache(maxsize=100)
def get_brand_template(brand: str, template: str) -> Response:
    return TemplateService.download_brand_template(
        tillo_client,
        query_params=create_brand_template_query_params(
            brand=brand,
            template=template,
        )
        .get_not_empty_values()
    )

async def read_brand_template(response: Response):
    async for chunk in response.aiter_bytes(8192):
        yield chunk