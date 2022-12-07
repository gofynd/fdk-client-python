"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CurrentStatus import CurrentStatus

from .Prices import Prices











from .AppliedPromos import AppliedPromos





from .FinancialBreakup import FinancialBreakup

from .Item import Item


class Bags(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    can_return = fields.Boolean(required=False)
    
    returnable_date = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    delivery_date = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    item = fields.Nested(Item, required=False)
    

