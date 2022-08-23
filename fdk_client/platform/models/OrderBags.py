"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderBrandName import OrderBrandName





from .FinancialBreakup import FinancialBreakup



from .BagConfigs import BagConfigs

from .BagGST import BagGST

from .OrderBagItem import OrderBagItem



from .OrderBagArticle import OrderBagArticle




class OrderBags(BaseSchema):
    # Orders swagger.json

    
    brand = fields.Nested(OrderBrandName, required=False)
    
    entity_type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    current_status = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    item = fields.Nested(OrderBagItem, required=False)
    
    bag_id = fields.Int(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    display_name = fields.Str(required=False)
    

