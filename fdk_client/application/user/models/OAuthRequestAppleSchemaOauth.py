"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class OAuthRequestAppleSchemaOauth(BaseSchema):
    #  swagger.json

    
    identity_token = fields.Str(required=False)
    
