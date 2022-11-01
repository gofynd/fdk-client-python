"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class InformationPhone(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
    number = fields.Str(required=False)
    
