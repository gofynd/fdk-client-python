"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ErrorCodeAndDescription import ErrorCodeAndDescription



class HttpErrorCodeAndResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    
