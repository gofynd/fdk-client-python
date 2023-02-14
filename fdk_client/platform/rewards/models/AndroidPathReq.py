"""rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AndroidPathReq(BaseSchema):
    #  swagger.json

    
    paths = fields.List(fields.Str(required=False), required=False)
    
