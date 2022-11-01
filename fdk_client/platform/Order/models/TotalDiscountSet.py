"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TotalDiscountSetPresentmentMoney import TotalDiscountSetPresentmentMoney



from .TotalDiscountSetShopMoney import TotalDiscountSetShopMoney



class TotalDiscountSet(BaseSchema):
    #  swagger.json

    
    presentment_money = fields.Nested(TotalDiscountSetPresentmentMoney, required=False)
    
    shop_money = fields.Nested(TotalDiscountSetShopMoney, required=False)
    
