"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Prices import Prices



from .Item import Item









from .CurrentStatus import CurrentStatus


class BagsData(BaseSchema):
    # Order swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    quantity = fields.Int(required=False)
    
    item = fields.Nested(Item, required=False)
    
    can_return = fields.Boolean(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    id = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Dict(required=False), required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    

