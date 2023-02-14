"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CartList(BaseSchema):
    #  swagger.json

    
    cart_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
