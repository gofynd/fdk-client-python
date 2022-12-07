"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CartDetailResponse import CartDetailResponse







class UpdateCartDetailResponse(BaseSchema):
    #  swagger.json

    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    