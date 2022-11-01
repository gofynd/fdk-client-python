"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TatacliqLuxury import TatacliqLuxury



class MarketplaceIdentifiers(BaseSchema):
    #  swagger.json

    
    tatacliq_luxury = fields.Nested(TatacliqLuxury, required=False)
    
