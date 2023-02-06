"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class TotalDiscountSetPresentmentMoney(BaseSchema):
    #  swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
