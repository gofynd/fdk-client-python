"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ManualAssignDPToShipmentResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Str(required=False)
    
    errors = fields.List(fields.Str(required=False), required=False)
    
