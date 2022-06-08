"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CreateOrderUserPaymentMethods import CreateOrderUserPaymentMethods








class CreateOrderUserRequest(BaseSchema):
    # Payment swagger.json

    
    payment_link_id = fields.Str(required=False)
    
    payment_methods = fields.Nested(CreateOrderUserPaymentMethods, required=False)
    
    currency = fields.Str(required=False)
    
    meta = fields.Str(required=False)
    
    return_url = fields.Str(required=False)
    

