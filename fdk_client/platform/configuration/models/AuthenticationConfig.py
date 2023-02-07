"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class AuthenticationConfig(BaseSchema):
    #  swagger.json

    
    required = fields.Boolean(required=False)
    
    provider = fields.Str(required=False)
    
