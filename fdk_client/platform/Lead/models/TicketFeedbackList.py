"""Lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TicketFeedback import TicketFeedback



class TicketFeedbackList(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(TicketFeedback, required=False), required=False)
    
