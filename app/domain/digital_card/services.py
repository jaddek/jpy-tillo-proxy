import logging

from httpx import Response
from jpy_tillo_sdk.domain.digital_card.services import IssueDigitalCodeService
from tillo.clients import tillo_client_async

logger = logging.getLogger(__name__)


async def issue_digital_code(body) -> Response:

    response = await IssueDigitalCodeService.issue_digital_code(
        tillo_client_async,
        body=body
    )

    return response

async def top_up(body) -> Response:
    pass

async def cancel_by_url(body) -> Response:
    pass

async def cancel_by_code(body) -> Response:
    pass

async def reverse(body) -> Response:
    pass

async def stock(body) -> Response:
    pass

async def balance(body) -> Response:
    pass

async def order(body) -> Response:
    pass

async def check(reference: str) -> Response:
    pass