"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .BagConfigs import BagConfigs









from .CurrentStatus import CurrentStatus







from .OrderBrandName import OrderBrandName



from .BagGST import BagGST



from .PlatformItem import PlatformItem





from .FinancialBreakup import FinancialBreakup





from .AppliedPromos import AppliedPromos





from .OrderBagArticle import OrderBagArticle



from .PlatformDeliveryAddress import PlatformDeliveryAddress



from .Prices import Prices





class OrderBags(BaseSchema):
    #  swagger.json

    
    line_number = fields.Int(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    identifier = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    quantity = fields.Int(required=False)
    
    bag_id = fields.Int(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    can_return = fields.Boolean(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    display_name = fields.Str(required=False)
    
