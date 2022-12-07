"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EwayBillResponse import EwayBillResponse

from .EinvoiceResponse import EinvoiceResponse


class GstCredentialsResponse(BaseSchema):
    # Serviceability swagger.json

    
    e_waybill = fields.Nested(EwayBillResponse, required=False)
    
    e_invoice = fields.Nested(EinvoiceResponse, required=False)
    

