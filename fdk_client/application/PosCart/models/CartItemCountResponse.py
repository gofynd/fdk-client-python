"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class CartItemCountResponse(BaseSchema):
    #  swagger.json

    
    user_cart_items_count = fields.Int(required=False)
    
