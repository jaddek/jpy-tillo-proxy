from typing import Optional, Annotated
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
    client_request_id: str
    brand: str
    face_value: FaceValue
    delivery_method: str
    fulfilment_by: str
    section: str


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
    tags: [str]


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

#
# class ProformaInvoiceBody(BaseModel):
#     company_name: Annotated[str, Body()]
#     address_line_1: Annotated[str, Body()]
#     post_code: Annotated[str, Body()]
#     address_line_2: Optional[str] = None
#     address_line_3: Optional[str] = None
#     address_line_4: Optional[str] = None
#     city: Optional[str] = None
#     county: Optional[str] = None
#     country: Optional[str] = None
#
#
# class TransferRequestBody(BaseModel):
#     float: Annotated[str, Body(
#         description="The float and currency field values must correspond to entries listed in our Brand Information check-float endpoint response - i.e. an existing currency and float relationship.eg universal-float & GBP, amazon & USD"
#     )]
#     currency: Annotated[str, Body()]
#     amount: Annotated[str, Body()]
#     finance_email: Optional[Annotated[str, Body(
#         description="A finance_email may optionally be supplied, to send the invoice to a different recipient than your standard finance user."
#     )]] = None
#     proforma_invoice: Optional[ProformaInvoiceBody] = None
#     payment_reference: Optional[Annotated[str, Body(
#         description="A payment_reference field may optionally be supplied, otherwise Tillo will generate a payment reference for the transfer request. Uniqueness will not be enforced on supplied references, although we urge clients to make each unique."
#     )]] = None
