"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Subscription import Subscription



class SubscriptionActivateRes(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(Subscription, required=False)
    
