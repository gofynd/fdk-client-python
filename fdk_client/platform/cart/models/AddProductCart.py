"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




























class AddProductCart(BaseSchema):
    #  swagger.json

    
    parent_item_identifiers = fields.Dict(required=False)
    
    display = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    pos = fields.Boolean(required=False)
    
    item_size = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    seller_id = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
