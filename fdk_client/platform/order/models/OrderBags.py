"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .BagConfigs import BagConfigs



from .AppliedPromos import AppliedPromos



from .PlatformItem import PlatformItem





from .OrderBrandName import OrderBrandName



from .Prices import Prices





from .BagGST import BagGST







from .OrderBagArticle import OrderBagArticle





from .PlatformDeliveryAddress import PlatformDeliveryAddress











from .CurrentStatus import CurrentStatus



from .FinancialBreakup import FinancialBreakup



class OrderBags(BaseSchema):
    #  swagger.json

    
    can_cancel = fields.Boolean(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    display_name = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    entity_type = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    line_number = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
