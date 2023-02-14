"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BagConfigs import BagConfigs







from .FinancialBreakup import FinancialBreakup

from .OrderBrandName import OrderBrandName

from .PlatformItem import PlatformItem





from .OrderBagArticle import OrderBagArticle





from .BagGST import BagGST





from .Prices import Prices

from .PlatformDeliveryAddress import PlatformDeliveryAddress



from .AppliedPromos import AppliedPromos


class OrderBags(BaseSchema):
    # Order swagger.json

    
    entity_type = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    identifier = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    bag_id = fields.Int(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    quantity = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    current_status = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    

