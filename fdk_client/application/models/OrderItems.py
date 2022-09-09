"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ShipmentResponse import ShipmentResponse










class OrderItems(BaseSchema):
    # Order swagger.json

    
    order_created_time = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    user_info = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    
    bags_for_reorder = fields.List(fields.Dict(required=False), required=False)
    

