"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *


































class ProductTemplate(Schema):

    
    modified_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    categories = fields.List(fields.Str(required=False), required=False)
    
    tag = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    is_physical = fields.Boolean(required=False)
    

