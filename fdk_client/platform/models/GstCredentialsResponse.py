"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EinvoiceResponse import EinvoiceResponse

from .EwayBillResponse import EwayBillResponse


class GstCredentialsResponse(BaseSchema):
    # Serviceability swagger.json

    
    e_invoice = fields.Nested(EinvoiceResponse, required=False)
    
    e_waybill = fields.Nested(EwayBillResponse, required=False)
    

