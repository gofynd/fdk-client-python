"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Prices import Prices





from .AppliedPromos import AppliedPromos





from .BagGST import BagGST







from .PlatformItem import PlatformItem





from .PlatformDeliveryAddress import PlatformDeliveryAddress



from .FinancialBreakup import FinancialBreakup



from .BagConfigs import BagConfigs









from .OrderBrandName import OrderBrandName







from .OrderBagArticle import OrderBagArticle



class OrderBags(BaseSchema):
    #  swagger.json

    
    can_cancel = fields.Boolean(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    can_return = fields.Boolean(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    line_number = fields.Int(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    current_status = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    display_name = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
