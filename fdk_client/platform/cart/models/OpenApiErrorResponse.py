"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class OpenApiErrorResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    