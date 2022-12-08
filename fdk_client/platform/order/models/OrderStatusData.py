"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ShipmentDetail import ShipmentDetail



from .OrderDetails1 import OrderDetails1





class OrderStatusData(BaseSchema):
    #  swagger.json

    
    shipment_details = fields.List(fields.Nested(ShipmentDetail, required=False), required=False)
    
    order_details = fields.Nested(OrderDetails1, required=False)
    
    errors = fields.List(fields.Str(required=False), required=False)
    
