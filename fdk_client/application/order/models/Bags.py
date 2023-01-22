"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .Prices import Prices



from .Item import Item







from .CurrentStatus import CurrentStatus















from .AppliedPromos import AppliedPromos



from .FinancialBreakup import FinancialBreakup



class Bags(BaseSchema):
    #  swagger.json

    
    returnable_date = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    item = fields.Nested(Item, required=False)
    
    quantity = fields.Int(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    delivery_date = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
