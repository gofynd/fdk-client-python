"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .CartCheckoutCustomMeta import CartCheckoutCustomMeta



from .StaffCheckout import StaffCheckout

























class CartCheckoutDetailRequest(BaseSchema):
    #  swagger.json

    
    aggregator = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    custom_meta = fields.List(fields.Nested(CartCheckoutCustomMeta, required=False), required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    payment_params = fields.Dict(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    ordering_store = fields.Int(required=False)
    
    address_id = fields.Str(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    
