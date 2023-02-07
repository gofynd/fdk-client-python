"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .CartProductIdentifer import CartProductIdentifer













class UpdateProductCart(BaseSchema):
    #  swagger.json

    
    item_index = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    item_id = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    item_size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
