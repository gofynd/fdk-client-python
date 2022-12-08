"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .PriorityEnum import PriorityEnum





from .TicketContent import TicketContent





class AddTicketPayload(BaseSchema):
    #  swagger.json

    
    created_by = fields.Dict(required=False)
    
    status = fields.Str(required=False)
    
    priority = fields.Str(required=False, validate=OneOf([val.value for val in PriorityEnum.__members__.values()]))
    
    category = fields.Str(required=False)
    
    content = fields.Nested(TicketContent, required=False)
    
    _custom_json = fields.Dict(required=False)
    
