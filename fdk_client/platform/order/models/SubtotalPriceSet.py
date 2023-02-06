"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SubtotalPriceSetShopMoney import SubtotalPriceSetShopMoney



from .SubtotalPriceSetPresentmentMoney import SubtotalPriceSetPresentmentMoney



class SubtotalPriceSet(BaseSchema):
    #  swagger.json

    
    shop_money = fields.Nested(SubtotalPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(SubtotalPriceSetPresentmentMoney, required=False)
    
