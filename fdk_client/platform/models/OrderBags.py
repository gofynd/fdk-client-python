"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AppliedPromos import AppliedPromos

from .FinancialBreakup import FinancialBreakup







from .PlatformItem import PlatformItem





from .BagConfigs import BagConfigs

from .OrderBrandName import OrderBrandName



from .Prices import Prices



from .OrderBagArticle import OrderBagArticle



from .BagGST import BagGST



from .PlatformDeliveryAddress import PlatformDeliveryAddress


class OrderBags(BaseSchema):
    # Orders swagger.json

    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    identifier = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    current_status = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    line_number = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    entity_type = fields.Str(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    display_name = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    bag_id = fields.Int(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    

