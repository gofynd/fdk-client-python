"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Participant import Participant



class GetParticipantsInsideVideoRoomResponse(BaseSchema):
    #  swagger.json

    
    participants = fields.List(fields.Nested(Participant, required=False), required=False)
    
