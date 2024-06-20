"""Webhook Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class ClickEventBatch(BaseSchema):
    pass


class ClickEventRequest(BaseSchema):
    pass


class ClickEventResponse(BaseSchema):
    pass





class ClickEventBatch(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    


class ClickEventRequest(BaseSchema):
    # Webhook swagger.json

    
    batch = fields.List(fields.Nested(ClickEventBatch, required=False), required=False)
    


class ClickEventResponse(BaseSchema):
    # Webhook swagger.json

    
    success_count = fields.Int(required=False)
    
    failed_count = fields.Int(required=False)
    
    failed_events = fields.List(fields.Nested(ClickEventBatch, required=False), required=False)
    


