"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BagConfigs import BagConfigs



from .OrderBrandName import OrderBrandName



from .PlatformItem import PlatformItem





from .CurrentStatus import CurrentStatus



from .AppliedPromos import AppliedPromos



from .OrderBagArticle import OrderBagArticle



from .Prices import Prices

















from .FinancialBreakup import FinancialBreakup



from .PlatformDeliveryAddress import PlatformDeliveryAddress





from .BagGST import BagGST





class OrderBags(BaseSchema):
    #  swagger.json

    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    line_number = fields.Int(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    quantity = fields.Int(required=False)
    
    entity_type = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    identifier = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    display_name = fields.Str(required=False)
    
