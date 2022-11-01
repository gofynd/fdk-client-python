"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SuccessMessageResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
