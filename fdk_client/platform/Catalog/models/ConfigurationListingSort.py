"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ConfigurationListingSortConfig import ConfigurationListingSortConfig





class ConfigurationListingSort(BaseSchema):
    #  swagger.json

    
    config = fields.List(fields.Nested(ConfigurationListingSortConfig, required=False), required=False)
    
    default_key = fields.Str(required=False)
    
