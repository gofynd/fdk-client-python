"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class OpenApiErrorResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    errors = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
