"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ErrorResponse(BaseSchema):
    #  swagger.json

    
    status = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    
