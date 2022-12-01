"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .TicketContext import TicketContext



from .CreatedOn import CreatedOn





from .TicketContent import TicketContent





from .TicketCategory import TicketCategory



from .TicketSubCategory import TicketSubCategory



from .TicketSourceEnum import TicketSourceEnum



from .Status import Status



from .Priority import Priority























class Ticket(BaseSchema):
    #  swagger.json

    
    context = fields.Nested(TicketContext, required=False)
    
    created_on = fields.Nested(CreatedOn, required=False)
    
    response_id = fields.Str(required=False)
    
    content = fields.Nested(TicketContent, required=False)
    
    ticket_id = fields.Str(required=False)
    
    category = fields.Nested(TicketCategory, required=False)
    
    sub_category = fields.Nested(TicketSubCategory, required=False)
    
    source = fields.Nested(TicketSourceEnum, required=False)
    
    status = fields.Nested(Status, required=False)
    
    priority = fields.Nested(Priority, required=False)
    
    created_by = fields.Dict(required=False)
    
    assigned_to = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_feedback_pending = fields.Boolean(required=False)
    
    integration = fields.Dict(required=False)
    
    avis_shipment_mapping = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
