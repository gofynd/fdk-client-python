"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .TicketContent import TicketContent


class AddTicketPayload(BaseSchema):
    # Lead swagger.json

    
    status = fields.Str(required=False)
    
    priority = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    content = fields.Nested(TicketContent, required=False)
    

