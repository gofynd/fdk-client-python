"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SessionListResponseInfo import SessionListResponseInfo



class SessionListResponseSchema(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(SessionListResponseInfo, required=False), required=False)
    
