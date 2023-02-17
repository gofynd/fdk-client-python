"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .OrderBrandName import OrderBrandName



from .FinancialBreakup import FinancialBreakup



from .BagGST import BagGST



from .PlatformDeliveryAddress import PlatformDeliveryAddress







from .PlatformItem import PlatformItem





from .BagConfigs import BagConfigs





from .CurrentStatus import CurrentStatus



from .Prices import Prices









from .OrderBagArticle import OrderBagArticle





from .AppliedPromos import AppliedPromos





class OrderBags(BaseSchema):
    #  swagger.json

    
    parent_promo_bags = fields.Dict(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    bag_id = fields.Int(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    display_name = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    quantity = fields.Int(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    entity_type = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    can_return = fields.Boolean(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    line_number = fields.Int(required=False)
    
