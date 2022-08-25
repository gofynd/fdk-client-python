"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Media2 import Media2



from .Hierarchy import Hierarchy

from .CategoryMapping import CategoryMapping
















class CategoryRequestBody(BaseSchema):
    # Catalog swagger.json

    
    media = fields.Nested(Media2, required=False)
    
    slug = fields.Str(required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    level = fields.Int(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    priority = fields.Int(required=False)
    

