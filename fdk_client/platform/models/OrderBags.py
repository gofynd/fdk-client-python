"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .OrderBrandName import OrderBrandName





from .BagGST import BagGST

from .OrderBagArticle import OrderBagArticle

from .FinancialBreakup import FinancialBreakup

from .OrderBagItem import OrderBagItem

from .BagConfigs import BagConfigs




class OrderBags(BaseSchema):
    # Orders swagger.json

    
    bag_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    display_name = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    item = fields.Nested(OrderBagItem, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    entity_type = fields.Str(required=False)
    

