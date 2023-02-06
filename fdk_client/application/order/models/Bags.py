"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .CurrentStatus import CurrentStatus





from .Prices import Prices









from .FinancialBreakup import FinancialBreakup







from .AppliedPromos import AppliedPromos







from .Item import Item



class Bags(BaseSchema):
    #  swagger.json

    
    parent_promo_bags = fields.Dict(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    returnable_date = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    delivery_date = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    id = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    
    item = fields.Nested(Item, required=False)
    
