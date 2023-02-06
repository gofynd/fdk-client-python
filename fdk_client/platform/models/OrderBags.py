"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OrderBrandName import OrderBrandName

from .BagGST import BagGST

from .BagConfigs import BagConfigs









from .PlatformDeliveryAddress import PlatformDeliveryAddress



from .AppliedPromos import AppliedPromos





from .Prices import Prices

from .FinancialBreakup import FinancialBreakup



from .OrderBagArticle import OrderBagArticle

from .PlatformItem import PlatformItem






class OrderBags(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Int(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    bag_id = fields.Int(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    can_return = fields.Boolean(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    entity_type = fields.Str(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    

