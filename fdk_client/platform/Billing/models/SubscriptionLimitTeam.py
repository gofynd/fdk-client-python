"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class SubscriptionLimitTeam(BaseSchema):
    #  swagger.json

    
    limit = fields.Int(required=False)
    
