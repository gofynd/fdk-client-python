"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .FeedbackResponseItem import FeedbackResponseItem











class TicketFeedback(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    ticket_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    response = fields.List(fields.Nested(FeedbackResponseItem, required=False), required=False)
    
    category = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
