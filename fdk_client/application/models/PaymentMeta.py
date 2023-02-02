"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class PaymentMeta(BaseSchema):
    # Cart swagger.json

    
    payment_gateway = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    

