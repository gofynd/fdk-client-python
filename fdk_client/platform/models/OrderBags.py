"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Prices import Prices

from .OrderBrandName import OrderBrandName

from .AppliedPromos import AppliedPromos











from .FinancialBreakup import FinancialBreakup

from .PlatformDeliveryAddress import PlatformDeliveryAddress

from .PlatformItem import PlatformItem

from .BagGST import BagGST

from .OrderBagArticle import OrderBagArticle









from .BagConfigs import BagConfigs


class OrderBags(BaseSchema):
    # Order swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    bag_id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    

