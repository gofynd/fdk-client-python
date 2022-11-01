"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PresentmentMoney import PresentmentMoney



from .ShopMoney import ShopMoney



class TotalDiscountsSet(BaseSchema):
    #  swagger.json

    
    presentment_money = fields.Nested(PresentmentMoney, required=False)
    
    shop_money = fields.Nested(ShopMoney, required=False)
    
