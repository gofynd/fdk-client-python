"""Cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CartDetailResponse import CartDetailResponse







class UpdateCartDetailResponse(BaseSchema):
    #  swagger.json

    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
