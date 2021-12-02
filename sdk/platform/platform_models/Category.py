"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .Hierarchy import Hierarchy









from .Media2 import Media2













from .CategoryMapping import CategoryMapping








class Category(BaseSchema):

    
    name = fields.Str(required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    level = fields.Int(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Dict(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    uid = fields.Int(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    

