"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class AttributeDetailsGroup(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    

