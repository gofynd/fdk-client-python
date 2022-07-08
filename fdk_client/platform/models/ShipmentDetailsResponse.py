"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Shipment import Shipment


class ShipmentDetailsResponse(BaseSchema):
    # Orders swagger.json

    
    success = fields.Boolean(required=False)
    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    

