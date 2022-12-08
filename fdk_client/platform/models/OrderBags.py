"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OrderBagArticle import OrderBagArticle



from .Prices import Prices



from .AppliedPromos import AppliedPromos





from .BagConfigs import BagConfigs

from .PlatformItem import PlatformItem

from .FinancialBreakup import FinancialBreakup

from .OrderBrandName import OrderBrandName

from .PlatformDeliveryAddress import PlatformDeliveryAddress









from .BagGST import BagGST


class OrderBags(BaseSchema):
    # Order swagger.json

    
    parent_promo_bags = fields.Dict(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    entity_type = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    current_status = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    quantity = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    

