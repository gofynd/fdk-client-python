"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SaveSubscriptionSetupIntentResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    