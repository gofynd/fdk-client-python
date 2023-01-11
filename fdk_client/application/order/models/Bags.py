"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .Item import Item





from .FinancialBreakup import FinancialBreakup







from .AppliedPromos import AppliedPromos





from .Prices import Prices







from .CurrentStatus import CurrentStatus





class Bags(BaseSchema):
    #  swagger.json

    
    returnable_date = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    item = fields.Nested(Item, required=False)
    
    line_number = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    can_return = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    delivery_date = fields.Str(required=False)
    
