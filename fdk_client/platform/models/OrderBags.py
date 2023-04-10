"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OrderBagArticle import OrderBagArticle





from .PlatformDeliveryAddress import PlatformDeliveryAddress

from .PlatformItem import PlatformItem



from .FinancialBreakup import FinancialBreakup





from .BagConfigs import BagConfigs



from .OrderBrandName import OrderBrandName

from .CurrentStatus import CurrentStatus



from .Prices import Prices



from .BagGST import BagGST



from .AppliedPromos import AppliedPromos


class OrderBags(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    quantity = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    can_return = fields.Boolean(required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    display_name = fields.Str(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    identifier = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    entity_type = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    bag_id = fields.Int(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    

