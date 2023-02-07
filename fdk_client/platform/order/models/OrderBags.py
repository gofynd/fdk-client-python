"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AppliedPromos import AppliedPromos



from .OrderBagArticle import OrderBagArticle













from .BagConfigs import BagConfigs





from .PlatformDeliveryAddress import PlatformDeliveryAddress





from .Prices import Prices



from .OrderBrandName import OrderBrandName



from .PlatformItem import PlatformItem



from .CurrentStatus import CurrentStatus





from .FinancialBreakup import FinancialBreakup



from .BagGST import BagGST







class OrderBags(BaseSchema):
    #  swagger.json

    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    display_name = fields.Str(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    line_number = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    can_return = fields.Boolean(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    bag_id = fields.Int(required=False)
    
