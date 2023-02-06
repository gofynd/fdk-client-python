"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ErrorResponse1(BaseSchema):
    #  swagger.json

    
    status = fields.Int(required=False)
    
    error_trace = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
