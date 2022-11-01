"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TotalShippingPriceSetShopMoney import TotalShippingPriceSetShopMoney



from .TotalShippingPriceSetPresentmentMoney import TotalShippingPriceSetPresentmentMoney



class TotalShippingPriceSet(BaseSchema):
    #  swagger.json

    
    shop_money = fields.Nested(TotalShippingPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalShippingPriceSetPresentmentMoney, required=False)
    
