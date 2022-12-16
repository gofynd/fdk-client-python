"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Item1 import Item1



from .Prices import Prices



from .CurrentStatus import CurrentStatus





from .FinancialBreakup import FinancialBreakup



from .AppliedPromos1 import AppliedPromos1



class Bags1(BaseSchema):
    #  swagger.json

    
    item = fields.Nested(Item1, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    id = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos1, required=False), required=False)
    
