"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .CreateOrderUserData import CreateOrderUserData









class CreateOrderUserResponse(BaseSchema):
    #  swagger.json

    
    order_id = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    
    data = fields.Nested(CreateOrderUserData, required=False)
    
    callback_url = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
