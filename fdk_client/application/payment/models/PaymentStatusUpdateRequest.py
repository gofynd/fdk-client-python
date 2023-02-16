"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema


























class PaymentStatusUpdateRequest(BaseSchema):
    #  swagger.json

    
    aggregator = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
