"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Hierarchy import Hierarchy



from .Media import Media













from .CategoryMapping import CategoryMapping



class CategoryRequestBody(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    media = fields.Nested(Media, required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    level = fields.Int(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
