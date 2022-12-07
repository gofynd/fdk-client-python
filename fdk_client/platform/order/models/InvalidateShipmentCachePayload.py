"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class InvalidateShipmentCachePayload(BaseSchema):
    #  swagger.json

    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
