"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Hierarchy import Hierarchy



from .CategoryMapping import CategoryMapping







from .Media2 import Media2









class CategoryRequestBody(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    level = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    name = fields.Str(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    priority = fields.Int(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
