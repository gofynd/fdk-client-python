"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TotalTaxSetShopMoney import TotalTaxSetShopMoney



from .TotalTaxSetPresentmentMoney import TotalTaxSetPresentmentMoney



class TotalTaxSet(BaseSchema):
    #  swagger.json

    
    shop_money = fields.Nested(TotalTaxSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalTaxSetPresentmentMoney, required=False)
    
