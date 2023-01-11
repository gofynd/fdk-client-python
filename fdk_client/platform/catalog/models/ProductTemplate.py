"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






































class ProductTemplate(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    categories = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    attributes_schema = fields.List(fields.Dict(required=False), required=False)
    
    tag = fields.Str(required=False)
    
