"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TicketHistory import TicketHistory










class TicketHistoryList(BaseSchema):
    # Lead swagger.json

    
    docs = fields.List(fields.Nested(TicketHistory, required=False), required=False)
    
    limit = fields.Int(required=False)
    
    page = fields.Int(required=False)
    
    pages = fields.Int(required=False)
    
    total = fields.Int(required=False)
    

