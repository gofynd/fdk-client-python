"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class OAuthRequestSchemaProfile(BaseSchema):
    #  swagger.json

    
    last_name = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    full_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
