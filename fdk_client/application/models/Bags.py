"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Prices import Prices







from .CurrentStatus import CurrentStatus

from .Item import Item





from .AppliedPromos import AppliedPromos





from .FinancialBreakup import FinancialBreakup


class Bags(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    returnable_date = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    item = fields.Nested(Item, required=False)
    
    delivery_date = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    id = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    

