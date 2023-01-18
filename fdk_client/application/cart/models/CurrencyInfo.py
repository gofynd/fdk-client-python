"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class CurrencyInfo(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    
