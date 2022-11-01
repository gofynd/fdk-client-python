"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SubscriptionLimitIntegrations(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    
