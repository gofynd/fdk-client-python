"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FinancialBreakup import FinancialBreakup

from .OrderBagArticle import OrderBagArticle





from .OrderBrandName import OrderBrandName

from .OrderBagItem import OrderBagItem

from .BagGST import BagGST





from .BagConfigs import BagConfigs




class OrderBags(BaseSchema):
    # Orders swagger.json

    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    quantity = fields.Int(required=False)
    
    bag_id = fields.Int(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    item = fields.Nested(OrderBagItem, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    display_name = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    current_status = fields.Str(required=False)
    

