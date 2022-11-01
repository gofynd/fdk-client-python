"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class TaxLinesPriceSetPresentmentMoney(BaseSchema):
    #  swagger.json

    
    currency_code = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    
