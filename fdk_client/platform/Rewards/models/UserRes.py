"""Rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Points import Points



from .RewardUser import RewardUser



class UserRes(BaseSchema):
    #  swagger.json

    
    points = fields.Nested(Points, required=False)
    
    user = fields.Nested(RewardUser, required=False)
    
