"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ApplicationServiceabilityConfig(BaseSchema):
    #  swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    channel_id = fields.Str(required=False)
    
