"""Lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class CreateVideoRoomResponse(BaseSchema):
    #  swagger.json

    
    unique_name = fields.Str(required=False)
    
