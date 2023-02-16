"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AppliedPromos import AppliedPromos





from .OrderBagArticle import OrderBagArticle



from .BagGST import BagGST





from .PlatformItem import PlatformItem



from .Prices import Prices





from .OrderBrandName import OrderBrandName



from .FinancialBreakup import FinancialBreakup



from .BagConfigs import BagConfigs





from .CurrentStatus import CurrentStatus













from .PlatformDeliveryAddress import PlatformDeliveryAddress





class OrderBags(BaseSchema):
    #  swagger.json

    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    line_number = fields.Int(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    entity_type = fields.Str(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    bag_id = fields.Int(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    display_name = fields.Str(required=False)
    
