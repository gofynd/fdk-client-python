"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .AttributeSchemaOverride import AttributeSchemaOverride






















class ProductTemplate(BaseSchema):
    # Catalog swagger.json

    
    created_by = fields.Dict(required=False)
    
    modified_by = fields.Dict(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    is_archived = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    attribute_schema_override = fields.List(fields.Nested(AttributeSchemaOverride, required=False), required=False)
    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    tag = fields.Str(required=False)
    
    categories = fields.List(fields.Str(required=False), required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    

