"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PlatformShipment import PlatformShipment



from .OrderDict import OrderDict


class ShipmentDetailsResponse(BaseSchema):
    # Order swagger.json

    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    order = fields.Nested(OrderDict, required=False)
    

