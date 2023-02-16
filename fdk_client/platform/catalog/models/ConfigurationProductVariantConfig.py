"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .ProductSize import ProductSize





class ConfigurationProductVariantConfig(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    size = fields.Nested(ProductSize, required=False)
    
    priority = fields.Int(required=False)
    
