"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OverrideCartItem import OverrideCartItem






















class OverrideCheckoutReq(BaseSchema):
    # Cart swagger.json

    
    cart_items = fields.List(fields.Nested(OverrideCartItem, required=False), required=False)
    
    billing_address = fields.Dict(required=False)
    
    currency_code = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False)
    
    order_type = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    shipping_address = fields.Dict(required=False)
    
    cart_id = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
