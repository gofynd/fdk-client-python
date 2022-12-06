"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class OfferPrice(BaseSchema):
    #  swagger.json

    
    marked = fields.Int(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    bulk_effective = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    effective = fields.Int(required=False)
    
