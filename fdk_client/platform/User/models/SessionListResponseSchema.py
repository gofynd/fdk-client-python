"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class SessionListResponseSchema(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Str(required=False), required=False)
    
