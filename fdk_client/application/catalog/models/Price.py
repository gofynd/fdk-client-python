"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class Price(BaseSchema):
    #  swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
