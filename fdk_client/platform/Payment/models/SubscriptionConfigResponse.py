"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class SubscriptionConfigResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    aggregator = fields.Str(required=False)
    
    config = fields.Dict(required=False)
    
