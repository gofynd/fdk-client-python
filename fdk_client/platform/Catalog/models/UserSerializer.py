"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class UserSerializer(BaseSchema):
    #  swagger.json

    
    user_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
