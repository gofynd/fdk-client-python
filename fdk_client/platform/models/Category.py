"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .CategoryMapping import CategoryMapping

from .GatedCategoryTypes import GatedCategoryTypes









from .Hierarchy import Hierarchy



from .Media2 import Media2








class Category(BaseSchema):
    # Catalog swagger.json

    
    priority = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    level = fields.Int(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    is_gated_category = fields.Boolean(required=False)
    
    is_gst_exempt = fields.Boolean(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    gated_category_types = fields.Nested(GatedCategoryTypes, required=False)
    
    _id = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    created_on = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Dict(required=False)
    

