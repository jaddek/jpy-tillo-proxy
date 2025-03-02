import logging

from httpx import Response
from jpy_tillo_sdk.domain.digital_card.services import IssueDigitalCodeService
from app.tillo.clients import tillo_client_async

logger = logging.getLogger(__name__)


async def issue_digital_code(body) -> Response:
    response = await IssueDigitalCodeService.issue_digital_code_async(
        tillo_client_async, body=body
    )

    return response


async def top_up(body) -> Response:
    response = await IssueDigitalCodeService.top_up_digital_code_async(
        tillo_client_async, body=body
    )

    return response


async def cancel_by_url(body) -> Response:
    response = await IssueDigitalCodeService.cancel_digital_url_async(
        tillo_client_async, body=body
    )

    return response


async def cancel_by_code(body) -> Response:
    response = await IssueDigitalCodeService.cancel_digital_code_async(
        tillo_client_async, body=body
    )

    return response


async def reverse(body) -> Response:
    response = await IssueDigitalCodeService.reverse_digital_code_async(
        tillo_client_async, body=body
    )

    return response


async def stock(query) -> Response:
    response = await IssueDigitalCodeService.check_stock_async(
        tillo_client_async, query_params=query
    )

    return response


async def balance(query) -> Response:
    response = await IssueDigitalCodeService.check_balance_async(
        tillo_client_async, query_params=query
    )

    return response


async def order(query) -> Response:
    response = await IssueDigitalCodeService.order_digital_code_async(
        tillo_client_async, query_params=query
    )

    return response


async def check(reference: str) -> Response:
    response = await IssueDigitalCodeService.check_digital_order_async(
        tillo_client_async, query_params={"reference": reference}
    )

    return response
