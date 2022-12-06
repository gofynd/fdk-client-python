"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















from .Hierarchy import Hierarchy















from .Media import Media





from .CategoryMapping import CategoryMapping





class Category(BaseSchema):
    #  swagger.json

    
    created_on = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Dict(required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Str(required=False)
    
    level = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    media = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    is_active = fields.Boolean(required=False)
    
