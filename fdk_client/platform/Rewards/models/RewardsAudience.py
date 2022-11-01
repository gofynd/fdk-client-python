"""Rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class RewardsAudience(BaseSchema):
    #  swagger.json

    
    header_user_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
