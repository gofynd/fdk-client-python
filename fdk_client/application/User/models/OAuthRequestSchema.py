"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .OAuthRequestSchemaOauth2 import OAuthRequestSchemaOauth2



from .OAuthRequestSchemaProfile import OAuthRequestSchemaProfile



class OAuthRequestSchema(BaseSchema):
    #  swagger.json

    
    is_signed_in = fields.Boolean(required=False)
    
    oauth2 = fields.Nested(OAuthRequestSchemaOauth2, required=False)
    
    profile = fields.Nested(OAuthRequestSchemaProfile, required=False)
    
