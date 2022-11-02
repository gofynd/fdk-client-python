"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ApplicationMeta(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    