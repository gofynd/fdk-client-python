"""theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Src(BaseSchema):
    #  swagger.json

    
    link = fields.Str(required=False)
    
