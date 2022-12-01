"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TotalPriceSetShopMoney import TotalPriceSetShopMoney



from .TotalPriceSetPresentmentMoney import TotalPriceSetPresentmentMoney



class TotalPriceSet(BaseSchema):
    #  swagger.json

    
    shop_money = fields.Nested(TotalPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalPriceSetPresentmentMoney, required=False)
    
