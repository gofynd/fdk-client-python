"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




























from .StaffCheckout import StaffCheckout







from .Files import Files









class CartPosCheckoutDetailRequest(BaseSchema):
    #  swagger.json

    
    pos = fields.Boolean(required=False)
    
    ordering_store = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    payment_mode = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    pick_at_store_uid = fields.Int(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    files = fields.List(fields.Nested(Files, required=False), required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    address_id = fields.Str(required=False)
    
    payment_params = fields.Dict(required=False)
    
