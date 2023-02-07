"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Subscription import Subscription



class SubscriptionStatus(BaseSchema):
    #  swagger.json

    
    is_enabled = fields.Boolean(required=False)
    
    subscription = fields.Nested(Subscription, required=False)
    
