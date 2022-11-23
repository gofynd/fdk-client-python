"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .CurrentStatus import CurrentStatus







from .Item1 import Item1







from .Prices1 import Prices1



class BagsData(BaseSchema):
    #  swagger.json

    
    can_cancel = fields.Boolean(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    can_return = fields.Boolean(required=False)
    
    financial_breakup = fields.List(fields.Dict(required=False), required=False)
    
    item = fields.Nested(Item1, required=False)
    
    quantity = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    prices = fields.Nested(Prices1, required=False)
    
