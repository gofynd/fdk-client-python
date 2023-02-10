"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .FinancialBreakup import FinancialBreakup



from .CurrentStatus import CurrentStatus



from .PlatformDeliveryAddress import PlatformDeliveryAddress



from .OrderBrandName import OrderBrandName









from .Prices import Prices







from .BagConfigs import BagConfigs





from .OrderBagArticle import OrderBagArticle





from .BagGST import BagGST



from .PlatformItem import PlatformItem





from .AppliedPromos import AppliedPromos





class OrderBags(BaseSchema):
    #  swagger.json

    
    identifier = fields.Str(required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    bag_id = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    display_name = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    can_return = fields.Boolean(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    entity_type = fields.Str(required=False)
    
