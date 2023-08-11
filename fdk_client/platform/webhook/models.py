"""Webhook Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class CancelResponse(BaseSchema):
    pass


class EventProcessRequest(BaseSchema):
    pass


class Event(BaseSchema):
    pass


class ManualRetryFailedResponse(BaseSchema):
    pass


class FailedEventsCountSuccessResponse(BaseSchema):
    pass


class EventCountItem(BaseSchema):
    pass


class RetryStatusResponse(BaseSchema):
    pass


class EventSuccessResponse(BaseSchema):
    pass


class EventProcessedSuccessResponse(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class EventProcessReportObject(BaseSchema):
    pass


class EventProcessReports(BaseSchema):
    pass


class PingWebhook(BaseSchema):
    pass


class PingWebhookResponse(BaseSchema):
    pass


class ReportFiltersPayload(BaseSchema):
    pass


class FilterValues(BaseSchema):
    pass


class FilterResponseObject(BaseSchema):
    pass


class EventConfigResponse(BaseSchema):
    pass


class EventConfig(BaseSchema):
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


class HistoryResponseObject(BaseSchema):
    pass


class HistoryResponse(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class AssociationDetails(BaseSchema):
    pass


class SubscriberResponse(BaseSchema):
    pass


class AuthMeta(BaseSchema):
    pass


class Association(BaseSchema):
    pass


class SubscriberConfig(BaseSchema):
    pass


class SubscriberConfigList(BaseSchema):
    pass





class CancelResponse(BaseSchema):
    # Webhook swagger.json

    
    code = fields.Int(required=False)
    


class EventProcessRequest(BaseSchema):
    # Webhook swagger.json

    
    search_text = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    subscriber_ids = fields.List(fields.Int(required=False), required=False)
    
    event = fields.List(fields.Nested(Event, required=False), required=False)
    


class Event(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


class ManualRetryFailedResponse(BaseSchema):
    # Webhook swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    stack_trace = fields.Str(required=False)
    


class FailedEventsCountSuccessResponse(BaseSchema):
    # Webhook swagger.json

    
    items = fields.List(fields.Nested(EventCountItem, required=False), required=False)
    


class EventCountItem(BaseSchema):
    # Webhook swagger.json

    
    status = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class RetryStatusResponse(BaseSchema):
    # Webhook swagger.json

    
    total_event = fields.Int(required=False)
    
    success_count = fields.Int(required=False)
    
    failure_count = fields.Int(required=False)
    
    status = fields.Str(required=False)
    


class EventSuccessResponse(BaseSchema):
    # Webhook swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class EventProcessedSuccessResponse(BaseSchema):
    # Webhook swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class Error(BaseSchema):
    # Webhook swagger.json

    
    error = fields.Str(required=False)
    


class EventProcessReportObject(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    response_code = fields.Int(required=False)
    
    response_message = fields.Str(required=False)
    
    data = fields.Str(required=False)
    
    attempt = fields.Int(required=False)
    
    last_attempted_on = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    response_time = fields.Int(required=False)
    


class EventProcessReports(BaseSchema):
    # Webhook swagger.json

    
    rows = fields.List(fields.Nested(EventProcessReportObject, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


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
    


class ReportFiltersPayload(BaseSchema):
    # Webhook swagger.json

    
    subscriber_ids = fields.List(fields.Int(required=False), required=False)
    


class FilterValues(BaseSchema):
    # Webhook swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    


class FilterResponseObject(BaseSchema):
    # Webhook swagger.json

    
    filter_name = fields.Str(required=False)
    
    values = fields.List(fields.Nested(FilterValues, required=False), required=False)
    


class EventConfigResponse(BaseSchema):
    # Webhook swagger.json

    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    


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
    


class ReportFilterResponse(BaseSchema):
    # Webhook swagger.json

    
    items = fields.List(fields.Nested(FilterResponseObject, required=False), required=False)
    


class HistoryPayload(BaseSchema):
    # Webhook swagger.json

    
    type = fields.Str(required=False)
    
    page_no = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    


class HistoryFilters(BaseSchema):
    # Webhook swagger.json

    
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
    


class HistoryResponseObject(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    association = fields.Nested(AssociationDetails, required=False)
    
    filters = fields.Nested(HistoryFilters, required=False)
    
    filename = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    upload_service_response = fields.Nested(UploadServiceObject, required=False)
    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class HistoryResponse(BaseSchema):
    # Webhook swagger.json

    
    items = fields.List(fields.Nested(HistoryResponseObject, required=False), required=False)
    


class Page(BaseSchema):
    # Webhook swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class AssociationDetails(BaseSchema):
    # Webhook swagger.json

    
    company_id = fields.Int(required=False)
    


class SubscriberResponse(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    email_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    


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
    


class SubscriberConfig(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    status = fields.Str(required=False)
    
    email_id = fields.Str(required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    event_id = fields.List(fields.Int(required=False), required=False)
    


class SubscriberConfigList(BaseSchema):
    # Webhook swagger.json

    
    items = fields.List(fields.Nested(SubscriberResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


