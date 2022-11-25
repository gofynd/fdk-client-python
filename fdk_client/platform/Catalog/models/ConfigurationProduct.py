"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ConfigurationProductSimilar import ConfigurationProductSimilar



from .ConfigurationProductVariant import ConfigurationProductVariant



class ConfigurationProduct(BaseSchema):
    #  swagger.json

    
    similar = fields.Nested(ConfigurationProductSimilar, required=False)
    
    variant = fields.Nested(ConfigurationProductVariant, required=False)
    
