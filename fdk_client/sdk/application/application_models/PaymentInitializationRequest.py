"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




















class PaymentInitializationRequest(BaseSchema):
    # Payment swagger.json

    
    timeout = fields.Int(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    virtual_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    
    polling_url = fields.Str(required=False)
    

