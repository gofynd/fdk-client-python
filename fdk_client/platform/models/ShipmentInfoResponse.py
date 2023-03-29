"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PlatformShipment import PlatformShipment




class ShipmentInfoResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    
    message = fields.Str(required=False)
    

