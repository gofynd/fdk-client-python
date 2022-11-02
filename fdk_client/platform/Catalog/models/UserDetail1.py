"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class UserDetail1(BaseSchema):
    #  swagger.json

    
    username = fields.Str(required=False)
    
    full_name = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
