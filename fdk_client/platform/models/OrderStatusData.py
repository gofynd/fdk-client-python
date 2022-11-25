"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderDetails import OrderDetails

from .ShipmentDetail import ShipmentDetail




class OrderStatusData(BaseSchema):
    # Order swagger.json

    
    order_details = fields.Nested(OrderDetails, required=False)
    
    shipment_details = fields.List(fields.Nested(ShipmentDetail, required=False), required=False)
    
    errors = fields.List(fields.Str(required=False), required=False)
    

