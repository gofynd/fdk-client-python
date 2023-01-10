"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class UserSerializer(BaseSchema):
    #  swagger.json

    
    contact = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
