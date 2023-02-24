"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PlatformDeliveryAddress import PlatformDeliveryAddress

from .OrderBrandName import OrderBrandName





from .PlatformItem import PlatformItem





from .BagConfigs import BagConfigs

from .AppliedPromos import AppliedPromos



from .OrderBagArticle import OrderBagArticle





from .BagGST import BagGST





from .FinancialBreakup import FinancialBreakup



from .Prices import Prices




class OrderBags(BaseSchema):
    # Order swagger.json

    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    quantity = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    entity_type = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    bag_id = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    current_status = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    line_number = fields.Int(required=False)
    

