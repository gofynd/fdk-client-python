"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ConfigurationListingSortConfig(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    