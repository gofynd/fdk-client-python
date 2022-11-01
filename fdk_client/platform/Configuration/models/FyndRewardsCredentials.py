"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class FyndRewardsCredentials(BaseSchema):
    #  swagger.json

    
    public_key = fields.Str(required=False)
    
