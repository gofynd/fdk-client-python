"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PaymentMethod import PaymentMethod











from .StaffCheckout import StaffCheckout











from .CustomerDetails import CustomerDetails










class CartCheckoutDetailV2Request(BaseSchema):
    # Cart swagger.json

    
    address_id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethod, required=False), required=False)
    
    merchant_code = fields.Str(required=False)
    
    custom_meta = fields.Dict(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    payment_mode = fields.Str(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    aggregator = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False)
    
    callback_url = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    customer_details = fields.Nested(CustomerDetails, required=False)
    
    billing_address_id = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    
    payment_params = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    

