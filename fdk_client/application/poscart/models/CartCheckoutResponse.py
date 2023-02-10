"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CheckCart import CheckCart

















class CartCheckoutResponse(BaseSchema):
    #  swagger.json

    
    cart = fields.Nested(CheckCart, required=False)
    
    data = fields.Dict(required=False)
    
    callback_url = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    app_intercept_url = fields.Str(required=False)
    
