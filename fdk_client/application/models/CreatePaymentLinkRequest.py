"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class CreatePaymentLinkRequest(BaseSchema):
    # Payment swagger.json

    
    email = fields.Str(required=False)
    
    external_order_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    amount = fields.Float(required=False)
    
    mobile_number = fields.Str(required=False)
    

