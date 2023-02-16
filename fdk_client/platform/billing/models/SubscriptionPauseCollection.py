"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SubscriptionPauseCollection(BaseSchema):
    #  swagger.json

    
    behavior = fields.Str(required=False)
    
    resume_at = fields.Str(required=False)
    
