"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .FinancialBreakup import FinancialBreakup







from .Prices import Prices

from .OrderBrandName import OrderBrandName

from .BagConfigs import BagConfigs

from .BagGST import BagGST

from .AppliedPromos import AppliedPromos







from .PlatformDeliveryAddress import PlatformDeliveryAddress







from .OrderBagArticle import OrderBagArticle

from .PlatformItem import PlatformItem

from .CurrentStatus import CurrentStatus


class OrderBags(BaseSchema):
    # Order swagger.json

    
    can_return = fields.Boolean(required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    identifier = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    line_number = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    bag_id = fields.Int(required=False)
    
    entity_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    

