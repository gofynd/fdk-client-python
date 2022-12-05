"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Item1 import Item1



from .FinancialBreakup import FinancialBreakup



from .AppliedPromos1 import AppliedPromos1







from .CurrentStatus import CurrentStatus











from .Prices import Prices









class Bags1(BaseSchema):
    #  swagger.json

    
    item = fields.Nested(Item1, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos1, required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    delivery_date = fields.Str(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    can_return = fields.Boolean(required=False)
    
    returnable_date = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    id = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    line_number = fields.Int(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    
