"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PlatformItem import PlatformItem



from .BagGST import BagGST







from .CurrentStatus import CurrentStatus







from .Prices import Prices



from .OrderBrandName import OrderBrandName





from .AppliedPromos import AppliedPromos







from .BagConfigs import BagConfigs



from .FinancialBreakup import FinancialBreakup



from .OrderBagArticle import OrderBagArticle



from .PlatformDeliveryAddress import PlatformDeliveryAddress









class OrderBags(BaseSchema):
    #  swagger.json

    
    item = fields.Nested(PlatformItem, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    can_return = fields.Boolean(required=False)
    
    bag_id = fields.Int(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    display_name = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    entity_type = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
