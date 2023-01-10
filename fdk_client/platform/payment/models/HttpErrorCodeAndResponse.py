"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ErrorCodeAndDescription import ErrorCodeAndDescription





class HttpErrorCodeAndResponse(BaseSchema):
    #  swagger.json

    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    
    success = fields.Boolean(required=False)
    
