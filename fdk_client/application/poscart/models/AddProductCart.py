"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




























class AddProductCart(BaseSchema):
    #  swagger.json

    
    item_id = fields.Int(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    display = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    pos = fields.Boolean(required=False)
    
    item_size = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
