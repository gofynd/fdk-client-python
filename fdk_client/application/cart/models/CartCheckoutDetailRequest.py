"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema


























from .StaffCheckout import StaffCheckout









from .CartCheckoutCustomMeta import CartCheckoutCustomMeta



class CartCheckoutDetailRequest(BaseSchema):
    #  swagger.json

    
    ordering_store = fields.Int(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    payment_params = fields.Dict(required=False)
    
    callback_url = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    merchant_code = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    billing_address = fields.Dict(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    extra_meta = fields.Dict(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Nested(CartCheckoutCustomMeta, required=False), required=False)
    