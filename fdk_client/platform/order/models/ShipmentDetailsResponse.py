"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .PlatformShipment import PlatformShipment



from .OrderDict import OrderDict





class ShipmentDetailsResponse(BaseSchema):
    #  swagger.json

    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    
    order = fields.Nested(OrderDict, required=False)
    
    success = fields.Boolean(required=False)
    
