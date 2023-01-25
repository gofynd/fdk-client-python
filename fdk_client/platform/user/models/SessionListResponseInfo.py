"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class SessionListResponseInfo(BaseSchema):
    #  swagger.json

    
    session_id = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    ip = fields.Str(required=False)
    
    domain = fields.Str(required=False)
    
    expire_in = fields.Str(required=False)
    
