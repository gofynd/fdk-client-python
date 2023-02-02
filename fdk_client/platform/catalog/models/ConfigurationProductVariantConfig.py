"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ProductSize import ProductSize













class ConfigurationProductVariantConfig(BaseSchema):
    #  swagger.json

    
    display_type = fields.Str(required=False)
    
    size = fields.Nested(ProductSize, required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
