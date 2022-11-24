"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Shipment import Shipment

from .OrderDict import OrderDict




class ShipmentDetailsResponse(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    order = fields.Nested(OrderDict, required=False)
    
    success = fields.Boolean(required=False)
    

