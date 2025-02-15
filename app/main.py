import logging
import sys

from dotenv import load_dotenv

from .routers import brands, floats

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

app.include_router(brands.router)
app.include_router(floats.router)


@app.get("/")
async def root():
    return {"message": "Tillo Proxy"}
