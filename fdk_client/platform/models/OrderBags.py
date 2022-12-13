"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagGST import BagGST

from .PlatformItem import PlatformItem



from .OrderBrandName import OrderBrandName









from .PlatformDeliveryAddress import PlatformDeliveryAddress

from .FinancialBreakup import FinancialBreakup

from .AppliedPromos import AppliedPromos





from .OrderBagArticle import OrderBagArticle

from .BagConfigs import BagConfigs





from .Prices import Prices






class OrderBags(BaseSchema):
    # Order swagger.json

    
    gst_details = fields.Nested(BagGST, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    identifier = fields.Str(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    current_status = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    line_number = fields.Int(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    entity_type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    bag_id = fields.Int(required=False)
    

