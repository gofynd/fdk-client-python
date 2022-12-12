"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagConfigs import BagConfigs

from .PlatformDeliveryAddress import PlatformDeliveryAddress

from .FinancialBreakup import FinancialBreakup

from .AppliedPromos import AppliedPromos



from .BagGST import BagGST





from .PlatformItem import PlatformItem



from .OrderBagArticle import OrderBagArticle

from .OrderBrandName import OrderBrandName











from .Prices import Prices


class OrderBags(BaseSchema):
    # Order swagger.json

    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    entity_type = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    display_name = fields.Str(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    current_status = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    

