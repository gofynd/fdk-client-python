"""Webhook Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema


















class EventPayload(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    event_trace_id = fields.Str(required=False)
    
    message_id = fields.Str(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    