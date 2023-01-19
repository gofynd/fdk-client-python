"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .OrderDict import OrderDict



from .PlatformShipment import PlatformShipment



class ShipmentDetailsResponse(BaseSchema):
    #  swagger.json

    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    order = fields.Nested(OrderDict, required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    
