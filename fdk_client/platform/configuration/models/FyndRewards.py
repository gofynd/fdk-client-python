"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .FyndRewardsCredentials import FyndRewardsCredentials



class FyndRewards(BaseSchema):
    #  swagger.json

    
    credentials = fields.Nested(FyndRewardsCredentials, required=False)
    
