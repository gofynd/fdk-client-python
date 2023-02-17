"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Media1 import Media1













class ProductVariants(BaseSchema):
    #  swagger.json

    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    category_uid = fields.Int(required=False)
    
    item_code = fields.Str(required=False)
    
