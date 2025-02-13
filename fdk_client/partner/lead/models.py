"""Lead Partner Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema


from .enums import *



class TicketList(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class TicketHistoryList(BaseSchema):
    pass


class EditTicketPayload(BaseSchema):
    pass


class AgentChangePayload(BaseSchema):
    pass


class GeneralConfigResponse(BaseSchema):
    pass


class SupportSchema(BaseSchema):
    pass


class SupportCommunicationSchema(BaseSchema):
    pass


class GeneralConfigIntegrationSchema(BaseSchema):
    pass


class Filter(BaseSchema):
    pass


class TicketHistoryPayload(BaseSchema):
    pass


class TicketContext(BaseSchema):
    pass


class CreatedOn(BaseSchema):
    pass


class TicketAsset(BaseSchema):
    pass


class TicketContent(BaseSchema):
    pass


class AddTicketPayload(BaseSchema):
    pass


class Priority(BaseSchema):
    pass


class SLA(BaseSchema):
    pass


class Status(BaseSchema):
    pass


class FeedbackForm(BaseSchema):
    pass


class TicketCategory(BaseSchema):
    pass


class TicketHistory(BaseSchema):
    pass


class Ticket(BaseSchema):
    pass


class Error4XX(BaseSchema):
    pass


class NotFoundError(BaseSchema):
    pass





class TicketList(BaseSchema):
    # Lead swagger.json

    
    items = fields.List(fields.Nested(Ticket, required=False), required=False)
    
    filters = fields.Nested(Filter, required=False)
    
    page = fields.Nested(Page, required=False)
    


class Page(BaseSchema):
    # Lead swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class TicketHistoryList(BaseSchema):
    # Lead swagger.json

    
    items = fields.List(fields.Nested(TicketHistory, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class EditTicketPayload(BaseSchema):
    # Lead swagger.json

    
    content = fields.Nested(TicketContent, required=False)
    
    category = fields.Str(required=False)
    
    sub_category = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    priority = fields.Str(required=False)
    
    assigned_to = fields.Nested(AgentChangePayload, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class AgentChangePayload(BaseSchema):
    # Lead swagger.json

    
    agent_id = fields.Str(required=False)
    


class GeneralConfigResponse(BaseSchema):
    # Lead swagger.json

    
    _id = fields.Str(required=False)
    
    support_communication = fields.List(fields.Nested(SupportCommunicationSchema, required=False), required=False)
    
    show_communication_info = fields.Boolean(required=False)
    
    show_support_dris = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    integration = fields.Nested(GeneralConfigIntegrationSchema, required=False)
    
    allow_ticket_creation = fields.Boolean(required=False)
    
    show_listing = fields.Boolean(required=False)
    
    available_integration = fields.List(fields.Str(required=False), required=False)
    
    enable_dris = fields.Boolean(required=False)
    
    support_email = fields.Nested(SupportSchema, required=False)
    
    support_phone = fields.Nested(SupportSchema, required=False)
    
    support_faq = fields.Nested(SupportSchema, required=False)
    


class SupportSchema(BaseSchema):
    # Lead swagger.json

    
    value = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    


class SupportCommunicationSchema(BaseSchema):
    # Lead swagger.json

    
    type = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    


class GeneralConfigIntegrationSchema(BaseSchema):
    # Lead swagger.json

    
    type = fields.Str(required=False)
    


class Filter(BaseSchema):
    # Lead swagger.json

    
    priorities = fields.List(fields.Nested(Priority, required=False), required=False)
    
    categories = fields.List(fields.Nested(TicketCategory, required=False), required=False)
    
    statuses = fields.List(fields.Nested(Status, required=False), required=False)
    
    assignees = fields.List(fields.Dict(required=False), required=False)
    
    all_categories = fields.Dict(required=False)
    


class TicketHistoryPayload(BaseSchema):
    # Lead swagger.json

    
    value = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    


class TicketContext(BaseSchema):
    # Lead swagger.json

    
    application_id = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    


class CreatedOn(BaseSchema):
    # Lead swagger.json

    
    user_agent = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    


class TicketAsset(BaseSchema):
    # Lead swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False, validate=OneOf([val.value for val in TicketAssetTypeEnum.__members__.values()]))
    


class TicketContent(BaseSchema):
    # Lead swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    attachments = fields.List(fields.Nested(TicketAsset, required=False), required=False)
    


class AddTicketPayload(BaseSchema):
    # Lead swagger.json

    
    created_by = fields.Dict(required=False)
    
    status = fields.Str(required=False)
    
    priority = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    content = fields.Nested(TicketContent, required=False)
    
    _custom_json = fields.Dict(required=False)
    


class Priority(BaseSchema):
    # Lead swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    color = fields.Str(required=False)
    


class SLA(BaseSchema):
    # Lead swagger.json

    
    resolution_time = fields.Str(required=False)
    


class Status(BaseSchema):
    # Lead swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    color = fields.Str(required=False)
    


class FeedbackForm(BaseSchema):
    # Lead swagger.json

    
    inputs = fields.Dict(required=False)
    
    title = fields.Str(required=False)
    
    timestamps = fields.Dict(required=False)
    


class TicketCategory(BaseSchema):
    # Lead swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    sub_categories = fields.List(fields.Nested(lambda: TicketCategory(exclude=('sub_categories')), required=False), required=False)
    
    group_id = fields.Float(required=False)
    
    feedback_form = fields.Nested(FeedbackForm, required=False)
    


class TicketHistory(BaseSchema):
    # Lead swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    
    ticket_id = fields.Str(required=False)
    
    created_on = fields.Nested(CreatedOn, required=False)
    
    created_by = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    


class Ticket(BaseSchema):
    # Lead swagger.json

    
    context = fields.Nested(TicketContext, required=False)
    
    created_on = fields.Nested(CreatedOn, required=False)
    
    response_id = fields.Str(required=False)
    
    content = fields.Nested(TicketContent, required=False)
    
    category = fields.Nested(TicketCategory, required=False)
    
    sub_category = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    status = fields.Nested(Status, required=False)
    
    priority = fields.Nested(Priority, required=False)
    
    sla = fields.Nested(SLA, required=False)
    
    created_by = fields.Dict(required=False)
    
    assigned_to = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    subscribers = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_feedback_pending = fields.Boolean(required=False)
    
    integration = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    additional_info = fields.List(fields.Dict(required=False), required=False)
    
    ticket_link = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    


class Error4XX(BaseSchema):
    # Lead swagger.json

    
    message = fields.Dict(required=False)
    
    stack = fields.Str(required=False)
    
    sentry = fields.Str(required=False)
    


class NotFoundError(BaseSchema):
    # Lead swagger.json

    
    message = fields.Str(required=False)
    


