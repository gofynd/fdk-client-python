"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderBagArticle import OrderBagArticle

from .AppliedPromos import AppliedPromos

from .PlatformItem import PlatformItem









from .Prices import Prices

from .BagConfigs import BagConfigs







from .FinancialBreakup import FinancialBreakup



from .OrderBrandName import OrderBrandName

from .BagGST import BagGST







from .PlatformDeliveryAddress import PlatformDeliveryAddress


class OrderBags(BaseSchema):
    # Orders swagger.json

    
    article = fields.Nested(OrderBagArticle, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    bag_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    entity_type = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    

