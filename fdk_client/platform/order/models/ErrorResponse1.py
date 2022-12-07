"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ErrorResponse1(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    
