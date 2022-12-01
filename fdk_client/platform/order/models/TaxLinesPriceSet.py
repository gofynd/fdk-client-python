"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TaxLinesPriceSetShopMoney import TaxLinesPriceSetShopMoney



from .TaxLinesPriceSetPresentmentMoney import TaxLinesPriceSetPresentmentMoney



class TaxLinesPriceSet(BaseSchema):
    #  swagger.json

    
    shop_money = fields.Nested(TaxLinesPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TaxLinesPriceSetPresentmentMoney, required=False)
    
