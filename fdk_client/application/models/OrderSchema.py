"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagsForReorder import BagsForReorder

from .Shipments import Shipments



from .BreakupValues import BreakupValues





from .UserInfo import UserInfo


class OrderSchema(BaseSchema):
    # Order swagger.json

    
    bags_for_reorder = fields.List(fields.Nested(BagsForReorder, required=False), required=False)
    
    shipments = fields.List(fields.Nested(Shipments, required=False), required=False)
    
    order_id = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    order_created_time = fields.Str(required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    

