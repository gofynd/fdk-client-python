"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .FinancialBreakup import FinancialBreakup







from .OrderBagArticle import OrderBagArticle







from .PlatformDeliveryAddress import PlatformDeliveryAddress







from .BagConfigs import BagConfigs



from .BagGST import BagGST





from .AppliedPromos import AppliedPromos







from .OrderBrandName import OrderBrandName



from .PlatformItem import PlatformItem



from .Prices import Prices







class OrderBags(BaseSchema):
    #  swagger.json

    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    can_return = fields.Boolean(required=False)
    
    entity_type = fields.Str(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    identifier = fields.Str(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    display_name = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    line_number = fields.Int(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    bag_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
