"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















from .Media2 import Media2



from .Hierarchy import Hierarchy













from .CategoryMapping import CategoryMapping





class Category(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    level = fields.Int(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    priority = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    created_by = fields.Dict(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    slug = fields.Str(required=False)
    
