"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CartCheckoutCustomMeta import CartCheckoutCustomMeta



from .StaffCheckout import StaffCheckout




























class CartCheckoutDetailRequest(BaseSchema):
    # Cart swagger.json

    
    payment_identifier = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Nested(CartCheckoutCustomMeta, required=False), required=False)
    
    billing_address = fields.Dict(required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    merchant_code = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False)
    
    address_id = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    payment_params = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    

