"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *











from .ProductSize import ProductSize




class ConfigurationProductConfig(Schema):

    
    key = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    size = fields.Nested(ProductSize, required=False)
    
    title = fields.Str(required=False)
    

