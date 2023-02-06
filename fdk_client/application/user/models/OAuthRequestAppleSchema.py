"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .OAuthRequestAppleSchemaOauth import OAuthRequestAppleSchemaOauth



from .OAuthRequestAppleSchemaProfile import OAuthRequestAppleSchemaProfile



class OAuthRequestAppleSchema(BaseSchema):
    #  swagger.json

    
    user_identifier = fields.Str(required=False)
    
    oauth = fields.Nested(OAuthRequestAppleSchemaOauth, required=False)
    
    profile = fields.Nested(OAuthRequestAppleSchemaProfile, required=False)
    
