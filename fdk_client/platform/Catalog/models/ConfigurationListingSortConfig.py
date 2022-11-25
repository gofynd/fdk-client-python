"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ConfigurationListingSortConfig(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
