"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PricesBreakup import PricesBreakup



from .BagsForReorder import BagsForReorder

from .UserInfo import UserInfo

from .ShipmentResponse import ShipmentResponse


class OrderItems(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    
    order_created_time = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(PricesBreakup, required=False), required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    bags_for_reorder = fields.List(fields.Nested(BagsForReorder, required=False), required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    

