"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderBrandName import OrderBrandName

from .OrderBagArticle import OrderBagArticle



from .BagGST import BagGST



from .PlatformItem import PlatformItem

from .BagConfigs import BagConfigs







from .AppliedPromos import AppliedPromos

from .PlatformDeliveryAddress import PlatformDeliveryAddress



from .FinancialBreakup import FinancialBreakup

from .Prices import Prices








class OrderBags(BaseSchema):
    # Order swagger.json

    
    brand = fields.Nested(OrderBrandName, required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    quantity = fields.Int(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    bag_id = fields.Int(required=False)
    
    entity_type = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    display_name = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    current_status = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    

