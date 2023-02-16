"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Participant import Participant



class GetParticipantsInsideVideoRoomResponse(BaseSchema):
    #  swagger.json

    
    participants = fields.List(fields.Nested(Participant, required=False), required=False)
    
