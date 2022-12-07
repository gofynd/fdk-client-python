"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .OrderDetails1 import OrderDetails1





from .ShipmentDetail import ShipmentDetail



class OrderStatusData(BaseSchema):
    #  swagger.json

    
    order_details = fields.Nested(OrderDetails1, required=False)
    
    errors = fields.List(fields.Str(required=False), required=False)
    
    shipment_details = fields.List(fields.Nested(ShipmentDetail, required=False), required=False)
    
