"""Lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class GetTokenForVideoRoomResponse(BaseSchema):
    #  swagger.json

    
    access_token = fields.Str(required=False)
    
