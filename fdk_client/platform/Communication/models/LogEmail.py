"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class LogEmail(BaseSchema):
    #  swagger.json

    
    template = fields.Str(required=False)
    
