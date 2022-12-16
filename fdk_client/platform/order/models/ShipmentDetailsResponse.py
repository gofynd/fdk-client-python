"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .OrderDict import OrderDict



from .PlatformShipment1 import PlatformShipment1







class ShipmentDetailsResponse(BaseSchema):
    #  swagger.json

    
    order = fields.Nested(OrderDict, required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment1, required=False), required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
