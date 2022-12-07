"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ShipmentidResponse import ShipmentidResponse



class ShipmentsResponse(BaseSchema):
    #  swagger.json

    
    shipment_id = fields.Nested(ShipmentidResponse, required=False)
    
