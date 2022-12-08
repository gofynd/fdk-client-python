"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CartItemMeta(BaseSchema):
    #  swagger.json

    
    primary_item = fields.Boolean(required=False)
    
    group_id = fields.Str(required=False)
    
