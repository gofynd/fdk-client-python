"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class SafetynetCredentials(BaseSchema):
    #  swagger.json

    
    api_key = fields.Str(required=False)
    
