"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagConfigs import BagConfigs



from .OrderBagItem import OrderBagItem





from .BagGST import BagGST



from .FinancialBreakup import FinancialBreakup

from .OrderBagArticle import OrderBagArticle

from .OrderBrandName import OrderBrandName




class OrderBags(BaseSchema):
    # Orders swagger.json

    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    entity_type = fields.Str(required=False)
    
    item = fields.Nested(OrderBagItem, required=False)
    
    current_status = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    quantity = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    bag_id = fields.Int(required=False)
    

