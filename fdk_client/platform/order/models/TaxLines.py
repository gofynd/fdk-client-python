"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .TaxLinesPriceSet import TaxLinesPriceSet



class TaxLines(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    price = fields.Str(required=False)
    
    rate = fields.Int(required=False)
    
    price_set = fields.Nested(TaxLinesPriceSet, required=False)
    
