"""Webhook Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema


from .enums import *



class EventConfig(BaseSchema):
    pass


class EventConfigList(BaseSchema):
    pass


class EventConfigResponse(BaseSchema):
    pass


class SubscriberConfigList(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class EventProcessedStatus(BaseSchema):
    pass


class EventPayload(BaseSchema):
    pass


class SubscriberConfig(BaseSchema):
    pass


class SubscriberResponse(BaseSchema):
    pass


class SubscriberEvent(BaseSchema):
    pass


class AuthMeta(BaseSchema):
    pass


class Association(BaseSchema):
    pass


class EventConfigBase(BaseSchema):
    pass





class EventConfig(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    


class EventConfigList(BaseSchema):
    # Webhook swagger.json

    
    items = fields.List(fields.Nested(EventConfig, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class EventConfigResponse(BaseSchema):
    # Webhook swagger.json

    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    


class SubscriberConfigList(BaseSchema):
    # Webhook swagger.json

    
    items = fields.List(fields.Nested(SubscriberResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Page(BaseSchema):
    # Webhook swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class EventProcessedStatus(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    attempt = fields.Int(required=False)
    
    response_code = fields.Str(required=False)
    
    response_message = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    processed_on = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    


class EventPayload(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    event_trace_id = fields.Str(required=False)
    
    message_id = fields.Str(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    


class SubscriberConfig(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    status = fields.Str(required=False, validate=OneOf([val.value for val in SubscriberStatus.__members__.values()]))
    
    email_id = fields.Str(required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    event_id = fields.List(fields.Int(required=False), required=False)
    


class SubscriberResponse(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    email_id = fields.Str(required=False)
    
    status = fields.Str(required=False, validate=OneOf([val.value for val in SubscriberStatus.__members__.values()]))
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    


class SubscriberEvent(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    subscriber_id = fields.Int(required=False)
    
    event_id = fields.Int(required=False)
    
    created_date = fields.Str(required=False)
    


class AuthMeta(BaseSchema):
    # Webhook swagger.json

    
    type = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    


class Association(BaseSchema):
    # Webhook swagger.json

    
    company_id = fields.Int(required=False)
    
    application_id = fields.List(fields.Str(required=False), required=False)
    
    extension_id = fields.Str(required=False)
    
    criteria = fields.Str(required=False)
    


class EventConfigBase(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


