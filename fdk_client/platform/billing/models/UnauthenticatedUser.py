"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class UnauthenticatedUser(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
