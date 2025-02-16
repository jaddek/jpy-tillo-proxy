from typing import Optional, Annotated
from fastapi import Body

from pydantic import BaseModel


class ProformaInvoiceBody(BaseModel):
    company_name: Annotated[str, Body()]
    address_line_1: Annotated[str, Body()]
    post_code: Annotated[str, Body()]
    address_line_2: Optional[str] = None
    address_line_3: Optional[str] = None
    address_line_4: Optional[str] = None
    city: Optional[str] = None
    county: Optional[str] = None
    country: Optional[str] = None


class TransferRequestBody(BaseModel):
    float: Annotated[str, Body(
        description="The float and currency field values must correspond to entries listed in our Brand Information check-float endpoint response - i.e. an existing currency and float relationship.eg universal-float & GBP, amazon & USD"
    )]
    currency: Annotated[str, Body()]
    amount: Annotated[str, Body()]
    finance_email: Optional[Annotated[str, Body(
        description="A finance_email may optionally be supplied, to send the invoice to a different recipient than your standard finance user."
    )]] = None
    proforma_invoice: Optional[ProformaInvoiceBody] = None
    payment_reference: Optional[Annotated[str, Body(
        description="A payment_reference field may optionally be supplied, otherwise Tillo will generate a payment reference for the transfer request. Uniqueness will not be enforced on supplied references, although we urge clients to make each unique."
    )]] = None
