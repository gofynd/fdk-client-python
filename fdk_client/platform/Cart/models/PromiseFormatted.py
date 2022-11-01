"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PromiseFormatted(BaseSchema):
    #  swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    
