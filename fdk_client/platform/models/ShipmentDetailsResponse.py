"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderDict import OrderDict





from .PlatformShipment import PlatformShipment


class ShipmentDetailsResponse(BaseSchema):
    # Order swagger.json

    
    order = fields.Nested(OrderDict, required=False)
    
    success = fields.Boolean(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    

