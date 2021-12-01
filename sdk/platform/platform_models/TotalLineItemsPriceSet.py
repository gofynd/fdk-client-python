"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .TotalLineItemsPriceSetShopMoney import TotalLineItemsPriceSetShopMoney

from .TotalLineItemsPriceSetPresentmentMoney import TotalLineItemsPriceSetPresentmentMoney


class TotalLineItemsPriceSet(BaseSchema):

    
    shop_money = fields.Nested(TotalLineItemsPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalLineItemsPriceSetPresentmentMoney, required=False)
    

