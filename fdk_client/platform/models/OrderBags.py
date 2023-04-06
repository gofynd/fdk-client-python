"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagConfigs import BagConfigs

from .CurrentStatus import CurrentStatus



from .OrderBrandName import OrderBrandName



from .PlatformDeliveryAddress import PlatformDeliveryAddress





from .OrderBagArticle import OrderBagArticle





from .BagGST import BagGST



from .FinancialBreakup import FinancialBreakup



from .Prices import Prices

from .AppliedPromos import AppliedPromos





from .PlatformItem import PlatformItem


class OrderBags(BaseSchema):
    # Order swagger.json

    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    entity_type = fields.Str(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    identifier = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    quantity = fields.Int(required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    can_return = fields.Boolean(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    

