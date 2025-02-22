from typing import Annotated

from fastapi import Body
from pydantic import BaseModel


class FaceValue(BaseModel):
    amount: str
    currency: str


class Personalisation(BaseModel):
    to_name: str
    from_name: str
    message: str
    template: str
    choice_link_theme: str


class FulfillmentParameters(BaseModel):
    to_name: str
    to_email: str
    from_email: str
    from_name: str
    subject: str
    language: str
    customer_id: str
    to_first_name: str
    to_last_name: str
    address_1: str
    address_2: str
    city: str
    postal_code: str
    country: str


class IssueDigitalCardStandardBody(BaseModel):
    client_request_id: Annotated[str, Body()]
    brand: Annotated[str, Body()]
    face_value: Annotated[FaceValue, Body()]
    delivery_method: Annotated[str, Body()]
    fulfilment_by: Annotated[str, Body()]
    section: Annotated[str, Body()]


class IssueDigitalCardWithPersonalisationBody(BaseModel):
    client_request_id: str
    brand: str
    face_value: str
    delivery_method: str
    fulfilment_by: str
    section: str
    personalisation: Personalisation


class IssueDigitalCardWithPersonalisationFulfilledByTilloBody(BaseModel):
    client_request_id: str
    brand: str
    face_value: str
    delivery_method: str
    fulfilment_by: str
    section: str
    personalisation: Personalisation
    fulfilment_parameters: FulfillmentParameters


class IssueReward(BaseModel):
    client_request_id: str
    brand: str
    face_value: FaceValue
    delivery_method: str
    fulfilment_by: str
    section: str
    personalisation: Personalisation
    fulfilment_parameters: FulfillmentParameters


class TopUpDigitalCodeBody(BaseModel):
    client_request_id: str
    brand: str
    face_value: FaceValue
    code: str
    pin: str
    sector: str
    serial_number: str


class CancelDigitalCodeBody(BaseModel):
    client_request_id: str
    original_client_request_id: str
    brand: str
    face_value: FaceValue
    code: str
    sector: str


class CancelDigitalUrlBody(BaseModel):
    client_request_id: str
    original_client_request_id: str
    brand: str
    face_value: FaceValue
    url: str
    sector: str


class ReverseDigitalCodeBody(BaseModel):
    client_request_id: str
    original_client_request_id: str
    brand: str
    face_value: FaceValue
    sector: str
    tags: list[str]


class BalanceCheckBody(BaseModel):
    client_request_id: str
    brand: str
    face_value: FaceValue
    code: str
    pin: str
    sector: str


class OrderDigitalCodeAsyncBody(BaseModel):
    client_request_id: str
    brand: str
    face_value: FaceValue
    delivery_method: str
    fulfilment_by: str
    section: str
    personalisation: Personalisation
    fulfilment_parameters: FulfillmentParameters
