"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .IntegrationOptIn import IntegrationOptIn



from .OtherEntity import OtherEntity



class OptedStoreIntegration(BaseSchema):
    #  swagger.json

    
    other_opted = fields.Boolean(required=False)
    
    other_integration = fields.Nested(IntegrationOptIn, required=False)
    
    other_entity = fields.Nested(OtherEntity, required=False)
    
