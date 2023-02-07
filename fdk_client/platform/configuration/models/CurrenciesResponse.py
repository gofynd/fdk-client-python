"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Currency import Currency



class CurrenciesResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(Currency, required=False), required=False)
    
