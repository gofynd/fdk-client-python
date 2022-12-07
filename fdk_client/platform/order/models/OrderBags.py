"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Prices import Prices



from .PlatformItem import PlatformItem





from .BagGST import BagGST



from .OrderBrandName import OrderBrandName





from .BagConfigs import BagConfigs





from .PlatformDeliveryAddress1 import PlatformDeliveryAddress1





from .FinancialBreakup import FinancialBreakup



from .AppliedPromos import AppliedPromos











from .OrderBagArticle import OrderBagArticle





class OrderBags(BaseSchema):
    #  swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    line_number = fields.Int(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    quantity = fields.Int(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress1, required=False)
    
    identifier = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    display_name = fields.Str(required=False)
    
