"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentResponse import ShipmentResponse

from .BagsForReorder import BagsForReorder

from .UserInfo1 import UserInfo1

from .PricesBreakup import PricesBreakup








class OrderItems(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    bags_for_reorder = fields.List(fields.Nested(BagsForReorder, required=False), required=False)
    
    user_info = fields.Nested(UserInfo1, required=False)
    
    breakup_values = fields.List(fields.Nested(PricesBreakup, required=False), required=False)
    
    order_id = fields.Str(required=False)
    
    order_created_time = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    

