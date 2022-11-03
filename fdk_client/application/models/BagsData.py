"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .CurrentStatus import CurrentStatus

from .Prices import Prices

from .Item import Item


class BagsData(BaseSchema):
    # Order swagger.json

    
    can_cancel = fields.Boolean(required=False)
    
    id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    financial_breakup = fields.List(fields.Dict(required=False), required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    item = fields.Nested(Item, required=False)
    

