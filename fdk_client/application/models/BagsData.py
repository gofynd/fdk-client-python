"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CurrentStatus import CurrentStatus



from .Item import Item







from .Prices import Prices




class BagsData(BaseSchema):
    # Order swagger.json

    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    can_return = fields.Boolean(required=False)
    
    item = fields.Nested(Item, required=False)
    
    financial_breakup = fields.List(fields.Dict(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    can_cancel = fields.Boolean(required=False)
    

