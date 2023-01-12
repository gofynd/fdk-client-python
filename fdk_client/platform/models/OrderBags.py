"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderBagArticle import OrderBagArticle





from .BagConfigs import BagConfigs



from .OrderBrandName import OrderBrandName



from .PlatformDeliveryAddress import PlatformDeliveryAddress

from .FinancialBreakup import FinancialBreakup



from .BagGST import BagGST



from .PlatformItem import PlatformItem





from .Prices import Prices

from .AppliedPromos import AppliedPromos








class OrderBags(BaseSchema):
    # Order swagger.json

    
    article = fields.Nested(OrderBagArticle, required=False)
    
    quantity = fields.Int(required=False)
    
    entity_type = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    line_number = fields.Int(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    bag_id = fields.Int(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    display_name = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    

