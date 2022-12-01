"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .TicketContent import TicketContent











from .PriorityEnum import PriorityEnum



from .AgentChangePayload import AgentChangePayload





class EditTicketPayload(BaseSchema):
    #  swagger.json

    
    content = fields.Nested(TicketContent, required=False)
    
    category = fields.Str(required=False)
    
    sub_category = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    priority = fields.Nested(PriorityEnum, required=False)
    
    assigned_to = fields.Nested(AgentChangePayload, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
