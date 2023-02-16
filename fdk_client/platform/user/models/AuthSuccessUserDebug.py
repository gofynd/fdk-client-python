"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AuthSuccessUserDebug(BaseSchema):
    #  swagger.json

    
    platform = fields.Str(required=False)
    
