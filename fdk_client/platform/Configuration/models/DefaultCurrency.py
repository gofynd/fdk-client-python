"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DefaultCurrency(BaseSchema):
    #  swagger.json

    
    ref = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
