"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ConfigurationProductVariant import ConfigurationProductVariant



from .ConfigurationProductSimilar import ConfigurationProductSimilar



class ConfigurationProduct(BaseSchema):
    #  swagger.json

    
    variant = fields.Nested(ConfigurationProductVariant, required=False)
    
    similar = fields.Nested(ConfigurationProductSimilar, required=False)
    
