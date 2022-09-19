"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .Media2 import Media2

from .Hierarchy import Hierarchy























from .GatedCategoryTypes import GatedCategoryTypes

from .CategoryMapping import CategoryMapping


class Category(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Str(required=False)
    
    level = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    media = fields.Nested(Media2, required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    is_gated_category = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    is_gst_exempt = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    gated_category_types = fields.Nested(GatedCategoryTypes, required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    

