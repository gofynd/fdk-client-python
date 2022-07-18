"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Hierarchy import Hierarchy

from .Media2 import Media2



from .CategoryMapping import CategoryMapping











from .GatedCategoryTypes import GatedCategoryTypes






















class Category(BaseSchema):
    # Catalog swagger.json

    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    media = fields.Nested(Media2, required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    modified_on = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    created_by = fields.Dict(required=False)
    
    gated_category_types = fields.Nested(GatedCategoryTypes, required=False)
    
    name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    is_gated_category = fields.Boolean(required=False)
    
    level = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    is_gst_exempt = fields.Boolean(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    

