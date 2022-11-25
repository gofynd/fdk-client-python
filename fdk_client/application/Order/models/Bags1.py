"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .FinancialBreakup import FinancialBreakup



from .AppliedPromos import AppliedPromos











from .Item1 import Item1





from .CurrentStatus import CurrentStatus







from .Prices import Prices



class Bags1(BaseSchema):
    #  swagger.json

    
    can_return = fields.Boolean(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    item = fields.Nested(Item1, required=False)
    
    returnable_date = fields.Str(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    delivery_date = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
