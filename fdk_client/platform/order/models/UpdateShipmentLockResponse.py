"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .CheckResponse import CheckResponse



class UpdateShipmentLockResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    check_response = fields.List(fields.Nested(CheckResponse, required=False), required=False)
    
