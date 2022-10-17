"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Media2 import Media2























from .Hierarchy import Hierarchy

from .CategoryMapping import CategoryMapping




class Category(BaseSchema):
    # Catalog swagger.json

    
    priority = fields.Int(required=False)
    
    level = fields.Int(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    slug = fields.Str(required=False)
    

