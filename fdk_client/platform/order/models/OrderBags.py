"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BagGST import BagGST











from .OrderBagArticle import OrderBagArticle



from .BagConfigs import BagConfigs









from .Prices import Prices



from .OrderBrandName import OrderBrandName



from .PlatformDeliveryAddress import PlatformDeliveryAddress



from .FinancialBreakup import FinancialBreakup









from .PlatformItem import PlatformItem





from .AppliedPromos import AppliedPromos



class OrderBags(BaseSchema):
    #  swagger.json

    
    gst_details = fields.Nested(BagGST, required=False)
    
    display_name = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    current_status = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    bag_id = fields.Int(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    entity_type = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
