"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CurrentStatus import CurrentStatus









from .AppliedPromos import AppliedPromos



from .Prices import Prices







from .FinancialBreakup import FinancialBreakup



from .Item1 import Item1











class Bags1(BaseSchema):
    #  swagger.json

    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    returnable_date = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    delivery_date = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    item = fields.Nested(Item1, required=False)
    
    id = fields.Int(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    
