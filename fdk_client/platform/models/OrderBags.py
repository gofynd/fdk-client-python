"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderBrandName import OrderBrandName





from .Prices import Prices

from .BagConfigs import BagConfigs



from .BagGST import BagGST



from .FinancialBreakup import FinancialBreakup





from .PlatformItem import PlatformItem

from .OrderBagArticle import OrderBagArticle

from .AppliedPromos import AppliedPromos



from .PlatformDeliveryAddress import PlatformDeliveryAddress






class OrderBags(BaseSchema):
    # Orders swagger.json

    
    brand = fields.Nested(OrderBrandName, required=False)
    
    quantity = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    current_status = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    identifier = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    display_name = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    

