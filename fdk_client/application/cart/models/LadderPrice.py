"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class LadderPrice(BaseSchema):
    #  swagger.json

    
    marked = fields.Int(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    offer_price = fields.Float(required=False)
    
    effective = fields.Int(required=False)
    
