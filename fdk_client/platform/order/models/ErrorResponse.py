"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ErrorResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error_trace = fields.Str(required=False)
    
