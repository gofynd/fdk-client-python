"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class UserInfo(BaseSchema):
    #  swagger.json

    
    uid = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
