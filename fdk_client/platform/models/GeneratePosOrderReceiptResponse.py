"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class GeneratePosOrderReceiptResponse(BaseSchema):
    # Order swagger.json

    
    invoice_receipt = fields.Str(required=False)
    
    payment_receipt = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    

