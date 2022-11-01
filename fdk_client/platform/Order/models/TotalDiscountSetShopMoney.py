"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class TotalDiscountSetShopMoney(BaseSchema):
    #  swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
