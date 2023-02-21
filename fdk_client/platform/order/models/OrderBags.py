"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .PlatformDeliveryAddress import PlatformDeliveryAddress







from .Prices import Prices



from .OrderBagArticle import OrderBagArticle



from .BagGST import BagGST



from .CurrentStatus import CurrentStatus





from .PlatformItem import PlatformItem









from .FinancialBreakup import FinancialBreakup



from .BagConfigs import BagConfigs



from .AppliedPromos import AppliedPromos









from .OrderBrandName import OrderBrandName



class OrderBags(BaseSchema):
    #  swagger.json

    
    quantity = fields.Int(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    line_number = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    can_return = fields.Boolean(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    display_name = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    entity_type = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
