"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .IntegrationLevel import IntegrationLevel



class UpdateIntegrationLevelRequest(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(IntegrationLevel, required=False), required=False)
    