"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Hierarchy import Hierarchy













from .Media2 import Media2

from .CategoryMapping import CategoryMapping














class Category(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    level = fields.Int(required=False)
    

