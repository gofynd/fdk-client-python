"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class InvalidateShipmentCacheNestedResponse(BaseSchema):
    #  swagger.json

    
    shipment_id = fields.Str(required=False)
    
    error = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
