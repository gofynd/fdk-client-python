"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .CreatedOn import CreatedOn











class TicketHistory(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    
    ticket_id = fields.Str(required=False)
    
    created_on = fields.Nested(CreatedOn, required=False)
    
    created_by = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
