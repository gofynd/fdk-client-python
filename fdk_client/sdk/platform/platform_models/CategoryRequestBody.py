"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .CategoryMapping import CategoryMapping







from .Hierarchy import Hierarchy







from .Media2 import Media2


class CategoryRequestBody(BaseSchema):
    # Catalog swagger.json

    
    departments = fields.List(fields.Int(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    is_active = fields.Boolean(required=False)
    
    level = fields.Int(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    priority = fields.Int(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    media = fields.Nested(Media2, required=False)
    

