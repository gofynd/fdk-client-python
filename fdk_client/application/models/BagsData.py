"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Prices import Prices









from .CurrentStatus import CurrentStatus



from .Item import Item


class BagsData(BaseSchema):
    # Order swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    financial_breakup = fields.List(fields.Dict(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    id = fields.Int(required=False)
    
    item = fields.Nested(Item, required=False)
    

