"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BagGST import BagGST



from .Prices import Prices



from .PlatformItem import PlatformItem





from .FinancialBreakup import FinancialBreakup





from .OrderBrandName import OrderBrandName





from .AppliedPromos import AppliedPromos









from .OrderBagArticle import OrderBagArticle







from .BagConfigs import BagConfigs





from .PlatformDeliveryAddress1 import PlatformDeliveryAddress1



class OrderBags(BaseSchema):
    #  swagger.json

    
    gst_details = fields.Nested(BagGST, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    display_name = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    bag_id = fields.Int(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    quantity = fields.Int(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    entity_type = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    identifier = fields.Str(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress1, required=False)
    
