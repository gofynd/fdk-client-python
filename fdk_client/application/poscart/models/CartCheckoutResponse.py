"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .CheckCart import CheckCart















class CartCheckoutResponse(BaseSchema):
    #  swagger.json

    
    app_intercept_url = fields.Str(required=False)
    
    cart = fields.Nested(CheckCart, required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    callback_url = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
