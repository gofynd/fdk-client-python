"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .AppliedPromos import AppliedPromos

from .FinancialBreakup import FinancialBreakup

from .BagGST import BagGST



from .Prices import Prices

from .PlatformDeliveryAddress import PlatformDeliveryAddress







from .OrderBrandName import OrderBrandName

from .OrderBagArticle import OrderBagArticle





from .BagConfigs import BagConfigs

from .PlatformItem import PlatformItem


class OrderBags(BaseSchema):
    # Order swagger.json

    
    display_name = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    bag_id = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    entity_type = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    

