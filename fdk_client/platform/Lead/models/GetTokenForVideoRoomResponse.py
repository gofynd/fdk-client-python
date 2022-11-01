"""Lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class GetTokenForVideoRoomResponse(BaseSchema):
    #  swagger.json

    
    access_token = fields.Str(required=False)
    
