"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class GtmCredentials(BaseSchema):
    #  swagger.json

    
    api_key = fields.Str(required=False)
    
