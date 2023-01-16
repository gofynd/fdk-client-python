"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Media2 import Media2





from .CategoryMapping import CategoryMapping





from .Hierarchy import Hierarchy













class CategoryRequestBody(BaseSchema):
    #  swagger.json

    
    level = fields.Int(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    is_active = fields.Boolean(required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    name = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    