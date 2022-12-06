"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .CategoryMapping import CategoryMapping











from .Media import Media





from .Hierarchy import Hierarchy















class Category(BaseSchema):
    #  swagger.json

    
    created_by = fields.Dict(required=False)
    
    level = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    modified_on = fields.Str(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    media = fields.Nested(Media, required=False)
    
    is_active = fields.Boolean(required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
