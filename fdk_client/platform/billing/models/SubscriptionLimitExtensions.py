"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SubscriptionLimitExtensions(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    
