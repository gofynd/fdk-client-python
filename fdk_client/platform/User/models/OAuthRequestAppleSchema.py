"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .OAuthRequestAppleSchemaOauth import OAuthRequestAppleSchemaOauth



from .OAuthRequestAppleSchemaProfile import OAuthRequestAppleSchemaProfile



class OAuthRequestAppleSchema(BaseSchema):
    #  swagger.json

    
    user_identifier = fields.Str(required=False)
    
    oauth = fields.Nested(OAuthRequestAppleSchemaOauth, required=False)
    
    profile = fields.Nested(OAuthRequestAppleSchemaProfile, required=False)
    
