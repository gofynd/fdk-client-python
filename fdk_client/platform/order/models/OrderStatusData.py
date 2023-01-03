"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .OrderDetails import OrderDetails



from .ShipmentDetail import ShipmentDetail



class OrderStatusData(BaseSchema):
    #  swagger.json

    
    errors = fields.List(fields.Str(required=False), required=False)
    
    order_details = fields.Nested(OrderDetails, required=False)
    
    shipment_details = fields.List(fields.Nested(ShipmentDetail, required=False), required=False)
    
