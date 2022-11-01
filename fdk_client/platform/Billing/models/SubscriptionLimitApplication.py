"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class SubscriptionLimitApplication(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
    hard_limit = fields.Int(required=False)
    
    soft_limit = fields.Int(required=False)
    
