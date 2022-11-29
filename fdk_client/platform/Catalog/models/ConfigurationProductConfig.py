"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ProductSize import ProductSize











class ConfigurationProductConfig(BaseSchema):
    #  swagger.json

    
    priority = fields.Int(required=False)
    
    subtitle = fields.Str(required=False)
    
    size = fields.Nested(ProductSize, required=False)
    
    key = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
