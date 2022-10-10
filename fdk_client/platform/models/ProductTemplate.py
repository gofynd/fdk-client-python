"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





























from .AttributeSchemaOverride import AttributeSchemaOverride










class ProductTemplate(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    tag = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    modified_by = fields.Dict(required=False)
    
    categories = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    attribute_schema = fields.List(fields.Nested(AttributeSchemaOverride, required=False), required=False)
    
    is_physical = fields.Boolean(required=False)
    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    multi_size = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    

