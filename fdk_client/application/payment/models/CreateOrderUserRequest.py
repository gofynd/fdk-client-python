"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CreateOrderUserPaymentMethods import CreateOrderUserPaymentMethods













class CreateOrderUserRequest(BaseSchema):
    #  swagger.json

    
    payment_methods = fields.Nested(CreateOrderUserPaymentMethods, required=False)
    
    payment_link_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    success_callback_url = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    failure_callback_url = fields.Str(required=False)
    
