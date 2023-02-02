"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ErrorDetail(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
