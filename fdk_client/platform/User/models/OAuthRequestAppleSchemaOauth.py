"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class OAuthRequestAppleSchemaOauth(BaseSchema):
    #  swagger.json

    
    identity_token = fields.Str(required=False)
    
