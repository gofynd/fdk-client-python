"""Webhook Partner Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema




class UpdateSubscriberRequest(BaseSchema):
    pass


class UpdateSubscriberResponse(BaseSchema):
    pass


class Association(BaseSchema):
    pass


class AuthMeta(BaseSchema):
    pass


class SubscriberEventMapping(BaseSchema):
    pass


class EventConfigResponse(BaseSchema):
    pass


class SubscriberConfigResponse(BaseSchema):
    pass


class InvalidEventsRequest(BaseSchema):
    pass


class InvalidEventsResponse(BaseSchema):
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


class HistoryPayload(BaseSchema):
    pass


class CancelDownloadResponse(BaseSchema):
    pass


class FilterReportResponse(BaseSchema):
    pass


class DeliveryTsResponse(BaseSchema):
    pass


class DeliveryTsSchema(BaseSchema):
    pass


class DeliveryDetailsRequest(BaseSchema):
    pass


class EventDeliveryDetailSchema(BaseSchema):
    pass


class DeliveryDetailsResponse(BaseSchema):
    pass


class EventProcessReportObject(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class DeliveryEventLevelSchema(BaseSchema):
    pass


class DeliverySummaryResponse(BaseSchema):
    pass


class DeliverySummarySchema(BaseSchema):
    pass


class ItemSchema(BaseSchema):
    pass





class UpdateSubscriberRequest(BaseSchema):
    # Webhook swagger.json

    
    status = fields.Str(required=False)
    


class UpdateSubscriberResponse(BaseSchema):
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
    


class SubscriberEventMapping(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    event_id = fields.Int(required=False)
    
    subscriber_id = fields.Int(required=False)
    
    topic = fields.Str(required=False, allow_none=True)
    
    created_on = fields.Str(required=False)
    


class EventConfigResponse(BaseSchema):
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
    
    group = fields.Str(required=False, allow_none=True)
    
    subscriber_event_mapping = fields.Nested(SubscriberEventMapping, required=False)
    


class SubscriberConfigResponse(BaseSchema):
    # Webhook swagger.json

    
    items = fields.List(fields.Nested(ItemSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class InvalidEventsRequest(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    


class InvalidEventsResponse(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    count = fields.Float(required=False)
    


class HistoryFilters(BaseSchema):
    # Webhook swagger.json

    
    events = fields.List(fields.Str(required=False), required=False)
    
    search_text = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    subscribers = fields.List(fields.Int(required=False), required=False)
    
    webhook_type = fields.List(fields.Str(required=False), required=False)
    


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
    


class HistoryPayload(BaseSchema):
    # Webhook swagger.json

    
    company_id = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    page_no = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    


class CancelDownloadResponse(BaseSchema):
    # Webhook swagger.json

    
    message = fields.Str(required=False)
    
    result = fields.Str(required=False)
    


class FilterReportResponse(BaseSchema):
    # Webhook swagger.json

    
    filter_name = fields.Str(required=False)
    
    values = fields.List(fields.Dict(required=False), required=False)
    


class DeliveryTsResponse(BaseSchema):
    # Webhook swagger.json

    
    delivery_ts = fields.List(fields.Nested(DeliveryTsSchema, required=False), required=False)
    


class DeliveryTsSchema(BaseSchema):
    # Webhook swagger.json

    
    timestamp = fields.Str(required=False)
    
    failed = fields.Float(required=False)
    
    removed_webhooks = fields.Float(required=False)
    
    success = fields.Float(required=False)
    


class DeliveryDetailsRequest(BaseSchema):
    # Webhook swagger.json

    
    company_id = fields.Str(required=False)
    
    page_no = fields.Float(required=False)
    
    page_size = fields.Float(required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    event = fields.List(fields.Nested(EventDeliveryDetailSchema, required=False), required=False)
    
    status = fields.Str(required=False)
    


class EventDeliveryDetailSchema(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    event_category = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


class DeliveryDetailsResponse(BaseSchema):
    # Webhook swagger.json

    
    rows = fields.List(fields.Nested(EventProcessReportObject, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class EventProcessReportObject(BaseSchema):
    # Webhook swagger.json

    
    event_name = fields.Str(required=False)
    
    response_code = fields.Int(required=False)
    
    response_message = fields.Str(required=False)
    
    data = fields.Str(required=False)
    
    attempt = fields.Int(required=False)
    
    last_attempted_on = fields.Float(required=False)
    
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
    


class DeliveryEventLevelSchema(BaseSchema):
    # Webhook swagger.json

    
    event = fields.Str(required=False)
    
    success = fields.Float(required=False)
    
    failed = fields.Float(required=False)
    
    failed_percentage = fields.Float(required=False)
    
    removed_webhooks = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    response_time = fields.Float(required=False)
    


class DeliverySummaryResponse(BaseSchema):
    # Webhook swagger.json

    
    delivery_event_level = fields.List(fields.Nested(DeliveryEventLevelSchema, required=False), required=False)
    
    delivery_summary = fields.Nested(DeliverySummarySchema, required=False)
    


class DeliverySummarySchema(BaseSchema):
    # Webhook swagger.json

    
    success = fields.Float(required=False)
    
    response_time = fields.Float(required=False)
    
    failed_percentage = fields.Float(required=False)
    
    removed_webhooks = fields.Float(required=False)
    


class ItemSchema(BaseSchema):
    # Webhook swagger.json

    
    id = fields.Int(required=False)
    
    modified_by = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    custom_headers = fields.Dict(required=False)
    
    status = fields.Str(required=False)
    
    email_id = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    type = fields.Str(required=False, allow_none=True)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    event_configs = fields.List(fields.Nested(EventConfigResponse, required=False), required=False)
    
    event_id = fields.List(fields.Int(required=False), required=False)
    


