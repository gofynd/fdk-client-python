"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SafetynetCredentials import SafetynetCredentials





class Safetynet(BaseSchema):
    #  swagger.json

    
    credentials = fields.Nested(SafetynetCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    
