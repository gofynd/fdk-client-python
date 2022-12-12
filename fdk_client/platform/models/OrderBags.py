"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .PlatformDeliveryAddress import PlatformDeliveryAddress



from .BagConfigs import BagConfigs



from .OrderBagArticle import OrderBagArticle







from .BagGST import BagGST

from .AppliedPromos import AppliedPromos



from .PlatformItem import PlatformItem

from .Prices import Prices

from .FinancialBreakup import FinancialBreakup



from .OrderBrandName import OrderBrandName


class OrderBags(BaseSchema):
    # Order swagger.json

    
    can_return = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    bag_id = fields.Int(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    entity_type = fields.Str(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    identifier = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    line_number = fields.Int(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    

