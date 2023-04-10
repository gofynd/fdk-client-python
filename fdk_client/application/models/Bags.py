"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CurrentStatus import CurrentStatus



from .Prices import Prices







from .FinancialBreakup import FinancialBreakup





from .AppliedPromos import AppliedPromos

from .Item import Item




class Bags(BaseSchema):
    # Order swagger.json

    
    can_cancel = fields.Boolean(required=False)
    
    returnable_date = fields.Str(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    delivery_date = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    can_return = fields.Boolean(required=False)
    
    id = fields.Int(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    item = fields.Nested(Item, required=False)
    
    quantity = fields.Int(required=False)
    

