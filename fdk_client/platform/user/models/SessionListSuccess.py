"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class SessionListSuccess(BaseSchema):
    #  swagger.json

    
    sessions = fields.List(fields.Str(required=False), required=False)
    
