"""Discount Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class UserDetails(BaseSchema):
    #  swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    