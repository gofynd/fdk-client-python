"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .ItemBrand import ItemBrand













class Item(BaseSchema):
    #  swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    brand = fields.Nested(ItemBrand, required=False)
    
    slug_key = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
