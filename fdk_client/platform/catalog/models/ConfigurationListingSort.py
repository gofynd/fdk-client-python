"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ConfigurationListingSortConfig import ConfigurationListingSortConfig



class ConfigurationListingSort(BaseSchema):
    #  swagger.json

    
    default_key = fields.Str(required=False)
    
    config = fields.List(fields.Nested(ConfigurationListingSortConfig, required=False), required=False)
    
