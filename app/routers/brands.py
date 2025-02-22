from datetime import datetime
from typing import Annotated

from app.domain.brand.services import (
    get_brands,
    get_brand_template_async,
    read_brand_template_async,
    get_brand_templates_async,
)
from app.domain.brand.query_filters import RouteBrandsParams
from fastapi import APIRouter, Query, Path
from starlette.responses import StreamingResponse

router = APIRouter(prefix="/brands", tags=["Brands"])


@router.get("")
async def brands(
    query: Annotated[
        RouteBrandsParams,
        Query(
            title="Brands",
            description="Brands Query Params",
        ),
    ],
):
    response = await get_brands(detail=query.detail)

    return response.json()


@router.get("/{brand}/templates")
async def brand_templates(
    brand: Annotated[
        str,
        Path(min_length=2, max_length=20, title="Brand name, for example 'amazon-de'"),
    ],
):
    response = await get_brand_templates_async(brand)

    return response.json()


@router.get("/{brand}/templates/{template}")
async def brand_template(
    brand: Annotated[
        str,
        Path(min_length=2, max_length=20, title="Brand name, for example 'amazon-de'"),
    ],
    template: Annotated[
        str,
        Path(
            title="Brand template",
            description="Template name, for example 'standard'",
            min_length=2,
            max_length=20,
        ),
    ],
):
    response = await get_brand_template_async(brand, template)
    date = datetime.now().strftime("%m-%d-%Y")

    return StreamingResponse(
        read_brand_template_async(response),
        media_type="application/zip",
        headers={
            "Content-Disposition": f"attachment; filename={brand}_template_{template}_{date}_archive.zip"
        },
    )
