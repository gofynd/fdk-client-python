"""webhook Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EventConfig import EventConfig



class EventConfigResponse(BaseSchema):
    #  swagger.json

    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    
