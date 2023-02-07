"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




































class PaymentInitializationResponse(BaseSchema):
    #  swagger.json

    
    aggregator = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    currency = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    polling_url = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    upi_poll_url = fields.Str(required=False)
    
    bqr_image = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    
    virtual_id = fields.Str(required=False)
    
