"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Item import Item





from .Prices import Prices

from .AppliedPromos import AppliedPromos



from .CurrentStatus import CurrentStatus



from .FinancialBreakup import FinancialBreakup


class BagsData(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    item = fields.Nested(Item, required=False)
    
    delivery_date = fields.Str(required=False)
    
    returnable_date = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    id = fields.Int(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    

