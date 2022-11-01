"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Currency import Currency



class CurrenciesResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(Currency, required=False), required=False)
    
