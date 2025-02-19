from typing import Annotated

from domain.digital_card.body_requests import IssueDigitalCardStandardBody, IssueDigitalCardWithPersonalisationBody, \
    IssueDigitalCardWithPersonalisationFulfilledByTilloBody, IssueReward, TopUpDigitalCodeBody, CancelDigitalUrlBody, \
    CancelDigitalCodeBody, ReverseDigitalCodeBody, BalanceCheckBody, OrderDigitalCodeAsyncBody
from fastapi import APIRouter, Body, Path

router = APIRouter(prefix="/card/digital", tags=["Digital Card"])


@router.post('/issue/digital_code')
async def issue_digital_code(
        body: Annotated[
            IssueDigitalCardStandardBody,
            Body(
                title="Issue a new digital gift card",
                description=""
            )
        ]
):
    return {"message": body}


@router.post('/issue/digital_code_with_personalisation')
async def issue_digital_code_with_personalisation(
        body: Annotated[
            IssueDigitalCardWithPersonalisationBody,
            Body(
                title="Issue a new digital gift card",
                description="You can add a personal touch to digital gift cards by passing additional \"personalisation\" parameters.  These include the recipients name, the senders name, and a short message. You can customise the theming of a choice link using the \"choice_link_theme\" parameter. "
            )
        ]
):
    return {"message": body}


@router.post('/issue/digital_code_fulfillment_by_tillo')
async def issue_digital_code_fulfillment_by_tillo(
        body: Annotated[
            IssueDigitalCardWithPersonalisationFulfilledByTilloBody,
            Body(
                title="Issue a new digital gift card",
                description="If you would like Tillo to take care of sending the gift card email to the end customer you can change the \"fulfilment_by\" parameter to \"rewardcloud\". You will also need to provide the additional \"fulfilment_parameters\". NOTE: Personalisation is also required when choosing fulfilment by Tillo."
            )
        ]
):
    return {"message": body}


@router.post('/issue/reward')
async def issue_reward(
        body: Annotated[
            IssueReward,
            Body(
                title="Issue a new Reward Pass by email or url",
                description=""
            )
        ]
):
    return {"message": body}


@router.post('/top-up')
async def topUp(
        body: Annotated[
            TopUpDigitalCodeBody,
            Body(
                title="Top up a digital gift card using the gift card number and pin.",
                description="The serial_number property is now mandatory for the Sainsbury (sainsburys ) brand."
            )
        ]
):
    return {"message": body}


@router.post('/cancel/url')
async def cancel_by_url(
        body: Annotated[
            CancelDigitalUrlBody,
            Body(
                title="Cancel an issued digital gift card",
                description=""
            )
        ]
):
    return {"message": body}


@router.post('/cancel/code')
async def cancel_by_code(
        body: Annotated[
            CancelDigitalCodeBody,
            Body(
                title="Cancel an issued digital gift card",
                description=""
            )
        ]
):
    return {"message": body}


@router.get('/reverse')
async def reverse(
        body: Annotated[
            ReverseDigitalCodeBody,
            Body(
                title="Reverse",
                description="Reverse a digital gift card. This endpoint allows you to cancel an issued digital gift card using just the original_client_request_id. This can be a useful alternative to cancel when your initial request timed out and may not neccesarily have access to the code or url from the issuance response. However, please note that this endpoint can only be used within 48 hours of the original issuance."
            )
        ]
):
    return {"message": body}


@router.get('/stock/{brand}')
async def stock(
        brand: Annotated[
            str,
            Path(
                min_length=2,
                max_length=20,
                title="Brand name, for example 'amazon-de'"
            )
        ],
):
    return {"message": brand}


@router.post('/balance')
async def balance(
        body: Annotated[
            BalanceCheckBody,
            Body(
                title="Reverse",
                description="Reverse a digital gift card. This endpoint allows you to cancel an issued digital gift card using just the original_client_request_id. This can be a useful alternative to cancel when your initial request timed out and may not neccesarily have access to the code or url from the issuance response. However, please note that this endpoint can only be used within 48 hours of the original issuance."
            )
        ]
):
    return {"message": body}


@router.post('/async/order')
async def order(
        body: Annotated[
            OrderDigitalCodeAsyncBody,
            Body(
                title="Create an asynchronous request for a gift code.",
                description=""
            )
        ]
):
    return {"message": body}


@router.get('/async/check/{reference}')
async def check(
        reference: Annotated[
            str,
            Path(
                min_length=36,
                max_length=36,
                title="Reference, for example 'af2ad340-cde0-11eb-bb06-b1ffbbb1a894'"
            )
        ],
):
    return {"message": reference}
