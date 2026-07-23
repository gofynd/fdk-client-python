"""Webhook Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class ClickEventBatch(BaseSchema):
    pass


class ClickEventPayload(BaseSchema):
    pass


class ClickEventDetails(BaseSchema):
    pass





class ClickEventBatch(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    


class ClickEventPayload(BaseSchema):
    # Webhook swagger.json

    
    batch = fields.List(fields.Nested(ClickEventBatch, required=False), required=False)
    
    sent_at = fields.Str(required=False)
    


class ClickEventDetails(BaseSchema):
    # Webhook swagger.json

    
    success_count = fields.Int(required=False)
    
    failed_count = fields.Int(required=False)
    
    failed_events = fields.List(fields.Nested(ClickEventBatch, required=False), required=False)
    


