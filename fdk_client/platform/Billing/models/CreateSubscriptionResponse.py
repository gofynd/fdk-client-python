"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EntitySubscription import EntitySubscription





class CreateSubscriptionResponse(BaseSchema):
    #  swagger.json

    
    subscription = fields.Nested(EntitySubscription, required=False)
    
    confirm_url = fields.Str(required=False)
    
