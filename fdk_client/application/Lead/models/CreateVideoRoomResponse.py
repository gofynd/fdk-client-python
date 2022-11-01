"""Lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class CreateVideoRoomResponse(BaseSchema):
    #  swagger.json

    
    unique_name = fields.Str(required=False)
    
