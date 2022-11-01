"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class SaveSubscriptionSetupIntentRequest(BaseSchema):
    #  swagger.json

    
    unique_external_id = fields.Str(required=False)
    
