from fastapi import APIRouter
from starlette.responses import StreamingResponse

from app.tillo.services import get_brands, get_brand_templates, get_brand_template, read_brand_template

router = APIRouter(prefix="/brands", tags=["Brands"])


@router.get("/tillo/brands")
async def brands():
    response = await get_brands()

    return response.json()


@router.get("/tillo/brands/{brand}/templates")
async def brand_templates(brand: str):
    response = await get_brand_templates(brand)

    return response.json()


@router.get("/tillo/brand/{brand}/templates/{template}")
async def brand_template(brand: str, template: str):
    response = await get_brand_template(brand, template)

    return StreamingResponse(read_brand_template(response), media_type="application/zip", headers={
        "Content-Disposition": "attachment; filename=my_archive.zip"
    })

