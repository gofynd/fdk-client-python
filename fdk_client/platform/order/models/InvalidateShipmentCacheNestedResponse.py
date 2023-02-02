"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class InvalidateShipmentCacheNestedResponse(BaseSchema):
    #  swagger.json

    
    status = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    
