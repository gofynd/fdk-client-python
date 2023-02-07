"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .NotifyUser import NotifyUser



class CreateVideoRoomPayload(BaseSchema):
    #  swagger.json

    
    unique_name = fields.Str(required=False)
    
    notify = fields.List(fields.Nested(NotifyUser, required=False), required=False)
    
