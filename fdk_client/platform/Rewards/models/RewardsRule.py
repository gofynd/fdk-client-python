"""Rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class RewardsRule(BaseSchema):
    #  swagger.json

    
    amount = fields.Float(required=False)
    
