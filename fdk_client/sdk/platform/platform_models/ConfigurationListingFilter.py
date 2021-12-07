"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .ConfigurationListingFilterConfig import ConfigurationListingFilterConfig


class ConfigurationListingFilter(BaseSchema):

    
    allow_single = fields.Boolean(required=False)
    
    attribute_config = fields.List(fields.Nested(ConfigurationListingFilterConfig, required=False), required=False)
    

