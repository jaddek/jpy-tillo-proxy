import logging
import app.config
from app.routers import brands, floats, digital_cards, physical_cards

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger("Proxy")

from fastapi import FastAPI  # noqa

app = FastAPI()

app.include_router(brands.router)
app.include_router(floats.router)
app.include_router(digital_cards.router)
app.include_router(physical_cards.router)


@app.get("/")
async def root():
    return {"message": "Hello, Tillo"}
