"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ConfigurationListingFilterConfig import ConfigurationListingFilterConfig





class ConfigurationListingFilter(BaseSchema):
    #  swagger.json

    
    attribute_config = fields.List(fields.Nested(ConfigurationListingFilterConfig, required=False), required=False)
    
    allow_single = fields.Boolean(required=False)
    
