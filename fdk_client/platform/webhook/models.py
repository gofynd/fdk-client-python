"""Webhook Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema


from .enums import *



class Error(BaseSchema):
    pass


class Event(BaseSchema):
    pass


class RetryEventRequest(BaseSchema):
    pass


class Item(BaseSchema):
    pass


class RetryCountResponse(BaseSchema):
    pass


class RetrySuccessResponse(BaseSchema):
    pass


class Err(BaseSchema):
    pass


class RetryFailureResponse(BaseSchema):
    pass


class RetryStatusResponse(BaseSchema):
    pass


class EventProcessRequest(BaseSchema):
    pass


class DownloadReportResponse(BaseSchema):
    pass


class EventProcessReports(BaseSchema):
    pass


class EventProcessReportObject(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class PingWebhook(BaseSchema):
    pass


class PingWebhookResponse(BaseSchema):
    pass


class EventConfig(BaseSchema):
    pass


class EventConfigResponse(BaseSchema):
    pass


class ReportFiltersPayload(BaseSchema):
    pass


class ReportFilterResponse(BaseSchema):
    pass


class HistoryPayload(BaseSchema):
    pass


class HistoryFilters(BaseSchema):
    pass


class Url(BaseSchema):
    pass


class CdnObject(BaseSchema):
    pass


class UploadServiceObject(BaseSchema):
    pass


class HistoryAssociation(BaseSchema):
    pass


class HistoryItems(BaseSchema):
    pass


class HistoryResponse(BaseSchema):
    pass


class CancelResponse(BaseSchema):
    pass


class Association(BaseSchema):
    pass


class AuthMeta(BaseSchema):
    pass


class SubscriberResponse(BaseSchema):
    pass


class Events(BaseSchema):
    pass


class SubscriberConfigRequestV2(BaseSchema):
    pass


class SubscriberConfig(BaseSchema):
    pass


class SubscriberConfigResponse(BaseSchema):
    pass


class SubscriberConfigList(BaseSchema):
    pass





class Error(BaseSchema):
    # Webhook swagger.json

    
    error = fields.Str(required=False)
    


class Event(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


class RetryEventRequest(BaseSchema):
    # Webhook swagger.json

    
    search_text = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    subscriber_ids = fields.List(fields.Int(required=False), required=False)
    
    event = fields.List(fields.Nested(Event, required=False), required=False)
    
    status = fields.Str(required=False)
    


class Item(BaseSchema):
    # Webhook swagger.json

    
    status = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class RetryCountResponse(BaseSchema):
    # Webhook swagger.json

    
    items = fields.List(fields.Nested(Item, required=False), required=False)
    


class RetrySuccessResponse(BaseSchema):
    # Webhook swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class Err(BaseSchema):
    # Webhook swagger.json

    
    msg = fields.Str(required=False)
    
    param = fields.Str(required=False)
    
    location = fields.Str(required=False)
    


class RetryFailureResponse(BaseSchema):
    # Webhook swagger.json

    
    err = fields.List(fields.Nested(Err, required=False), required=False)
    


class RetryStatusResponse(BaseSchema):
    # Webhook swagger.json

    
    total_event = fields.Int(required=False)
    
    success_count = fields.Int(required=False)
    
    failure_count = fields.Int(required=False)
    
    status = fields.Str(required=False)
    


class EventProcessRequest(BaseSchema):
    # Webhook swagger.json

    
    search_text = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    subscriber_ids = fields.List(fields.Int(required=False), required=False)
    
    status = fields.Str(required=False)
    
    event = fields.List(fields.Nested(Event, required=False), required=False)
    


class DownloadReportResponse(BaseSchema):
    # Webhook swagger.json

    
    file_name = fields.Str(required=False)
    


class EventProcessReports(BaseSchema):
    # Webhook swagger.json

    
    rows = fields.List(fields.Nested(EventProcessReportObject, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class EventProcessReportObject(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    response_code = fields.Int(required=False)
    
    response_message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    attempt = fields.Int(required=False)
    
    last_attempted_on = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    response_time = fields.Int(required=False)
    
    message_id = fields.Str(required=False)
    
    event_trace_id = fields.Str(required=False)
    


class Page(BaseSchema):
    # Webhook swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class PingWebhook(BaseSchema):
    # Webhook swagger.json

    
    webhook_url = fields.Str(required=False)
    
    auth_meta = fields.Dict(required=False)
    
    custom_headers = fields.Dict(required=False)
    


class PingWebhookResponse(BaseSchema):
    # Webhook swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    code = fields.Int(required=False)
    


class EventConfig(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    event_schema = fields.Dict(required=False, allow_none=True)
    
    version = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    description = fields.Str(required=False, allow_none=True)
    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    


class EventConfigResponse(BaseSchema):
    # Webhook swagger.json

    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    


class ReportFiltersPayload(BaseSchema):
    # Webhook swagger.json

    
    subscriber_ids = fields.List(fields.Int(required=False), required=False)
    


class ReportFilterResponse(BaseSchema):
    # Webhook swagger.json

    
    filter_name = fields.Str(required=False)
    
    values = fields.List(fields.Dict(required=False), required=False)
    


class HistoryPayload(BaseSchema):
    # Webhook swagger.json

    
    type = fields.Str(required=False)
    
    page_no = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    


class HistoryFilters(BaseSchema):
    # Webhook swagger.json

    
    events = fields.List(fields.Str(required=False), required=False)
    
    search_text = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    subscribers = fields.List(fields.Int(required=False), required=False)
    


class Url(BaseSchema):
    # Webhook swagger.json

    
    url = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class CdnObject(BaseSchema):
    # Webhook swagger.json

    
    urls = fields.List(fields.Nested(Url, required=False), required=False)
    


class UploadServiceObject(BaseSchema):
    # Webhook swagger.json

    
    cdn = fields.Nested(CdnObject, required=False)
    


class HistoryAssociation(BaseSchema):
    # Webhook swagger.json

    
    company_id = fields.Int(required=False)
    
    subscriber_ids = fields.List(fields.Int(required=False), required=False)
    


class HistoryItems(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    association = fields.Nested(HistoryAssociation, required=False)
    
    filters = fields.Nested(HistoryFilters, required=False)
    
    filename = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    upload_service_response = fields.Nested(UploadServiceObject, required=False)
    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False)
    


class HistoryResponse(BaseSchema):
    # Webhook swagger.json

    
    items = fields.List(fields.Nested(HistoryItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CancelResponse(BaseSchema):
    # Webhook swagger.json

    
    message = fields.Str(required=False)
    


class Association(BaseSchema):
    # Webhook swagger.json

    
    company_id = fields.Int(required=False)
    
    application_id = fields.List(fields.Str(required=False), required=False)
    
    extension_id = fields.Str(required=False)
    
    criteria = fields.Str(required=False)
    


class AuthMeta(BaseSchema):
    # Webhook swagger.json

    
    type = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    


class SubscriberResponse(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    modified_by = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
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
    


class SubscriberConfigRequestV2(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    status = fields.Str(required=False)
    
    email_id = fields.Str(required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    events = fields.List(fields.Nested(Events, required=False), required=False)
    


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
    


class SubscriberConfigResponse(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    modified_by = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
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

    
    items = fields.List(fields.Nested(SubscriberResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


