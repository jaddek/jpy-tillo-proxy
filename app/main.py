import logging
import sys

from dotenv import load_dotenv
from starlette.responses import StreamingResponse

from app.tillo.services import get_brands, get_brand_templates, get_brand_template, read_brand_template

load_dotenv(override=False)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter(
    "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s")
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

from fastapi import FastAPI

app = FastAPI()


@app.get("/tillo/brands")
def read_root():
    return get_brands().json()


@app.get("/tillo/brand/{brand}/templates")
def read_root(brand: str):
    return get_brand_templates(brand).json()


@app.get("/tillo/brand/{brand}/templates/{template}")
async def read_root(brand: str, template: str):
    response = get_brand_template(brand, template)

    return StreamingResponse(read_brand_template(response), media_type="application/zip", headers={
        "Content-Disposition": "attachment; filename=my_archive.zip"
    })
