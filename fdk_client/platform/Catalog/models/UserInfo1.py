"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class UserInfo1(BaseSchema):
    #  swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
