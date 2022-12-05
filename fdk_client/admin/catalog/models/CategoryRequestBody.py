"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .CategoryMapping import CategoryMapping













from .Hierarchy import Hierarchy



from .Media import Media







class CategoryRequestBody(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    priority = fields.Int(required=False)
    
    level = fields.Int(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    media = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
