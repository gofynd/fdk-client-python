"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Prices import Prices



from .AppliedPromos import AppliedPromos

from .PlatformDeliveryAddress import PlatformDeliveryAddress









from .BagConfigs import BagConfigs

from .BagGST import BagGST

from .FinancialBreakup import FinancialBreakup



from .OrderBagArticle import OrderBagArticle

from .PlatformItem import PlatformItem



from .OrderBrandName import OrderBrandName


class OrderBags(BaseSchema):
    # Orders swagger.json

    
    display_name = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    bag_id = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    line_number = fields.Int(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    can_return = fields.Boolean(required=False)
    
    current_status = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    entity_type = fields.Str(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    

