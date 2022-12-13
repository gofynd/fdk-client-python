"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BagsForReorder import BagsForReorder



from .Shipments import Shipments

from .UserInfo import UserInfo



from .BreakupValues import BreakupValues


class OrderSchema(BaseSchema):
    # Order swagger.json

    
    order_created_time = fields.Str(required=False)
    
    bags_for_reorder = fields.List(fields.Nested(BagsForReorder, required=False), required=False)
    
    order_id = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(Shipments, required=False), required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    

