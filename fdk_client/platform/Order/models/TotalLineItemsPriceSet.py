"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TotalLineItemsPriceSetShopMoney import TotalLineItemsPriceSetShopMoney



from .TotalLineItemsPriceSetPresentmentMoney import TotalLineItemsPriceSetPresentmentMoney



class TotalLineItemsPriceSet(BaseSchema):
    #  swagger.json

    
    shop_money = fields.Nested(TotalLineItemsPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalLineItemsPriceSetPresentmentMoney, required=False)
    
