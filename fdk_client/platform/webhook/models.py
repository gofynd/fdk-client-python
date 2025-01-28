"""Webhook Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema


from .enums import *



class Page(BaseSchema):
    pass


class BroadcasterConfig(BaseSchema):
    pass


class SubscriberEventMapping(BaseSchema):
    pass


class FilterSchema(BaseSchema):
    pass


class EventConfig(BaseSchema):
    pass


class EventConfigResult(BaseSchema):
    pass


class Association(BaseSchema):
    pass


class AssociationResp(BaseSchema):
    pass


class AuthMeta(BaseSchema):
    pass


class SubscriberDetails(BaseSchema):
    pass


class Events(BaseSchema):
    pass


class SubscriberConfigPostRequestV2(BaseSchema):
    pass


class SubscriberConfigUpdateRequestV2(BaseSchema):
    pass


class SubscriberConfigPost(BaseSchema):
    pass


class SubscriberConfigUpdate(BaseSchema):
    pass


class SubscriberConfigResult(BaseSchema):
    pass


class SubscriberConfigList(BaseSchema):
    pass


class RestEventData(BaseSchema):
    pass


class RestConfig(BaseSchema):
    pass


class QueueEventData(BaseSchema):
    pass


class KafkaConfig(BaseSchema):
    pass


class PubSubConfig(BaseSchema):
    pass


class TemporalEventData(BaseSchema):
    pass


class TemporalConfig(BaseSchema):
    pass


class SqsEventData(BaseSchema):
    pass


class SqsConfig(BaseSchema):
    pass


class EventBridgeData(BaseSchema):
    pass


class EventBridgeConfig(BaseSchema):
    pass


class EventMapBody(BaseSchema):
    pass


class WebhookConfig(BaseSchema):
    pass


class UpsertSubscriberConfig(BaseSchema):
    pass


class UpsertSubscriberConfigResult(BaseSchema):
    pass





class Page(BaseSchema):
    # Webhook swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class BroadcasterConfig(BaseSchema):
    # Webhook swagger.json

    
    topic = fields.Str(required=False)
    
    queue = fields.Str(required=False)
    
    event_bridge_name = fields.Str(required=False)
    
    workflow_name = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    detail_type = fields.Str(required=False)
    


class SubscriberEventMapping(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Float(required=False)
    
    event_id = fields.Float(required=False)
    
    subscriber_id = fields.Float(required=False)
    
    filters = fields.Nested(FilterSchema, required=False)
    
    reducer = fields.Dict(required=False, allow_none=True)
    
    broadcaster_config = fields.Nested(BroadcasterConfig, required=False)
    
    created_on = fields.Str(required=False)
    


class FilterSchema(BaseSchema):
    # Webhook swagger.json

    
    query = fields.Str(required=False)
    
    condition = fields.Str(required=False)
    
    logic = fields.Str(required=False)
    
    conditions = fields.List(fields.Dict(required=False), required=False)
    


class EventConfig(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    type = fields.Str(required=False, allow_none=True)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    subscriber_event_mapping = fields.Nested(SubscriberEventMapping, required=False)
    
    event_schema = fields.Dict(required=False, allow_none=True)
    
    group = fields.Str(required=False, allow_none=True)
    
    version = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    description = fields.Str(required=False, allow_none=True)
    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    


class EventConfigResult(BaseSchema):
    # Webhook swagger.json

    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    


class Association(BaseSchema):
    # Webhook swagger.json

    
    application_id = fields.List(fields.Str(required=False), required=False)
    
    extension_id = fields.Str(required=False)
    
    criteria = fields.Str(required=False)
    


class AssociationResp(BaseSchema):
    # Webhook swagger.json

    
    company_id = fields.Int(required=False)
    
    application_id = fields.List(fields.Str(required=False), required=False)
    
    extension_id = fields.Str(required=False)
    
    criteria = fields.Str(required=False)
    


class AuthMeta(BaseSchema):
    # Webhook swagger.json

    
    type = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    


class SubscriberDetails(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    modified_by = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(AssociationResp, required=False)
    
    custom_headers = fields.Dict(required=False, allow_none=True)
    
    status = fields.Str(required=False, validate=OneOf([val.value for val in SubscriberStatus.__members__.values()]))
    
    email_id = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    type = fields.Str(required=False, allow_none=True)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    


class Events(BaseSchema):
    # Webhook swagger.json

    
    slug = fields.Str(required=False)
    
    topic = fields.Str(required=False)
    
    queue = fields.Str(required=False)
    
    event_bridge_name = fields.Str(required=False)
    
    workflow_name = fields.Str(required=False)
    
    detail_type = fields.Str(required=False)
    


class SubscriberConfigPostRequestV2(BaseSchema):
    # Webhook swagger.json

    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False, allow_none=True)
    
    webhook_url = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    status = fields.Str(required=False, validate=OneOf([val.value for val in SubscriberStatus.__members__.values()]))
    
    email_id = fields.Str(required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    events = fields.List(fields.Nested(Events, required=False), required=False)
    


class SubscriberConfigUpdateRequestV2(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False, allow_none=True)
    
    webhook_url = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    status = fields.Str(required=False, validate=OneOf([val.value for val in SubscriberStatus.__members__.values()]))
    
    email_id = fields.Str(required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    events = fields.List(fields.Nested(Events, required=False), required=False)
    


class SubscriberConfigPost(BaseSchema):
    # Webhook swagger.json

    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False, allow_none=True)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    status = fields.Str(required=False, validate=OneOf([val.value for val in SubscriberStatus.__members__.values()]))
    
    email_id = fields.Str(required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    event_id = fields.List(fields.Int(required=False), required=False)
    


class SubscriberConfigUpdate(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False, allow_none=True)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    status = fields.Str(required=False, validate=OneOf([val.value for val in SubscriberStatus.__members__.values()]))
    
    email_id = fields.Str(required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    event_id = fields.List(fields.Int(required=False), required=False)
    


class SubscriberConfigResult(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    modified_by = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    association = fields.Nested(AssociationResp, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    status = fields.Str(required=False, validate=OneOf([val.value for val in SubscriberStatus.__members__.values()]))
    
    email_id = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    type = fields.Str(required=False, allow_none=True)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    event_id = fields.List(fields.Int(required=False), required=False)
    


class SubscriberConfigList(BaseSchema):
    # Webhook swagger.json

    
    items = fields.List(fields.Nested(SubscriberDetails, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class RestEventData(BaseSchema):
    # Webhook swagger.json

    
    event_category = fields.Str(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    version = fields.Float(required=False)
    


class RestConfig(BaseSchema):
    # Webhook swagger.json

    
    webhook_url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    custom_headers = fields.Dict(required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    events = fields.List(fields.Nested(RestEventData, required=False), required=False)
    


class QueueEventData(BaseSchema):
    # Webhook swagger.json

    
    event_category = fields.Str(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    version = fields.Float(required=False)
    
    topic = fields.Str(required=False)
    


class KafkaConfig(BaseSchema):
    # Webhook swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    events = fields.List(fields.Nested(QueueEventData, required=False), required=False)
    


class PubSubConfig(BaseSchema):
    # Webhook swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    events = fields.List(fields.Nested(QueueEventData, required=False), required=False)
    


class TemporalEventData(BaseSchema):
    # Webhook swagger.json

    
    event_category = fields.Str(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    version = fields.Float(required=False)
    
    queue = fields.Str(required=False)
    
    workflow_name = fields.Str(required=False)
    


class TemporalConfig(BaseSchema):
    # Webhook swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    events = fields.List(fields.Nested(TemporalEventData, required=False), required=False)
    


class SqsEventData(BaseSchema):
    # Webhook swagger.json

    
    event_category = fields.Str(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    version = fields.Float(required=False)
    
    queue = fields.Str(required=False)
    


class SqsConfig(BaseSchema):
    # Webhook swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    events = fields.List(fields.Nested(SqsEventData, required=False), required=False)
    


class EventBridgeData(BaseSchema):
    # Webhook swagger.json

    
    event_category = fields.Str(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    version = fields.Float(required=False)
    
    event_bridge_name = fields.Str(required=False)
    


class EventBridgeConfig(BaseSchema):
    # Webhook swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    events = fields.List(fields.Nested(EventBridgeData, required=False), required=False)
    


class EventMapBody(BaseSchema):
    # Webhook swagger.json

    
    rest = fields.Nested(RestConfig, required=False)
    
    kafka = fields.Nested(KafkaConfig, required=False)
    
    pub_sub = fields.Nested(PubSubConfig, required=False)
    
    temporal = fields.Nested(TemporalConfig, required=False)
    
    sqs = fields.Nested(SqsConfig, required=False)
    
    event_bridge = fields.Nested(EventBridgeConfig, required=False)
    


class WebhookConfig(BaseSchema):
    # Webhook swagger.json

    
    notification_email = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    event_map = fields.Nested(EventMapBody, required=False)
    


class UpsertSubscriberConfig(BaseSchema):
    # Webhook swagger.json

    
    webhook_config = fields.Nested(WebhookConfig, required=False)
    


class UpsertSubscriberConfigResult(BaseSchema):
    # Webhook swagger.json

    
    status = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


