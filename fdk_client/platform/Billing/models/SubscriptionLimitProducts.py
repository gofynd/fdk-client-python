"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SubscriptionLimitProducts(BaseSchema):
    #  swagger.json

    
    bulk = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    
