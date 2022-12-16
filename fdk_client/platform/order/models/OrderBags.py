"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Prices import Prices







from .BagGST import BagGST











from .OrderBagArticle import OrderBagArticle





from .OrderBrandName import OrderBrandName



from .BagConfigs import BagConfigs





from .FinancialBreakup import FinancialBreakup







from .PlatformDeliveryAddress1 import PlatformDeliveryAddress1



from .PlatformItem import PlatformItem



from .AppliedPromos import AppliedPromos





class OrderBags(BaseSchema):
    #  swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    entity_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    current_status = fields.Str(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    line_number = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress1, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    can_return = fields.Boolean(required=False)
    
