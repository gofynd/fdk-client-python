"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Item import Item

from .Prices import Prices

from .CurrentStatus import CurrentStatus



from .FinancialBreakup import FinancialBreakup


class Bags(BaseSchema):

    
    item = fields.Nested(Item, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    id = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    

