"""Common Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class LocationDefaultLanguage(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
