"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .Item1 import Item1











from .FinancialBreakup import FinancialBreakup





from .Prices import Prices





from .AppliedPromos import AppliedPromos



from .CurrentStatus import CurrentStatus





class Bags1(BaseSchema):
    #  swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    item = fields.Nested(Item1, required=False)
    
    id = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    returnable_date = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    delivery_date = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    line_number = fields.Int(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
