"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class OAuthRequestSchemaOauth2(BaseSchema):
    #  swagger.json

    
    access_token = fields.Str(required=False)
    
    expiry = fields.Int(required=False)
    
    refresh_token = fields.Str(required=False)
    
