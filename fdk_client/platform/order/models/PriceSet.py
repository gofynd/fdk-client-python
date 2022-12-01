"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PriceSetShopMoney import PriceSetShopMoney



from .PriceSetPresentmentMoney import PriceSetPresentmentMoney



class PriceSet(BaseSchema):
    #  swagger.json

    
    shop_money = fields.Nested(PriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(PriceSetPresentmentMoney, required=False)
    
