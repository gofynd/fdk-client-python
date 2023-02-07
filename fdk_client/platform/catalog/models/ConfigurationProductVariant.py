"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ConfigurationProductVariantConfig import ConfigurationProductVariantConfig



class ConfigurationProductVariant(BaseSchema):
    #  swagger.json

    
    config = fields.List(fields.Nested(ConfigurationProductVariantConfig, required=False), required=False)
    
