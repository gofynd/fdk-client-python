"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .FyndRewardsCredentials import FyndRewardsCredentials



class FyndRewards(BaseSchema):
    #  swagger.json

    
    credentials = fields.Nested(FyndRewardsCredentials, required=False)
    
