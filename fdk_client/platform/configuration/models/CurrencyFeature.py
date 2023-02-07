"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CurrencyFeature(BaseSchema):
    #  swagger.json

    
    value = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    default_currency = fields.Str(required=False)
    
