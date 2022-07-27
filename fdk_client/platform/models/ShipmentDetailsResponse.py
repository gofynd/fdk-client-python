"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderDict import OrderDict

from .Shipment import Shipment




class ShipmentDetailsResponse(BaseSchema):
    # Orders swagger.json

    
    order = fields.Nested(OrderDict, required=False)
    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
