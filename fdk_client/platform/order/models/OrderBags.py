"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Prices import Prices







from .BagConfigs import BagConfigs



from .AppliedPromos import AppliedPromos



from .OrderBagArticle import OrderBagArticle



from .OrderBrandName import OrderBrandName





from .CurrentStatus import CurrentStatus



from .BagGST import BagGST







from .FinancialBreakup import FinancialBreakup





from .PlatformDeliveryAddress import PlatformDeliveryAddress





from .PlatformItem import PlatformItem



class OrderBags(BaseSchema):
    #  swagger.json

    
    identifier = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    line_number = fields.Int(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    can_return = fields.Boolean(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    bag_id = fields.Int(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
