"""Lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema


from .enums import *



class TicketList(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class TicketHistoryList(BaseSchema):
    pass


class CustomFormList(BaseSchema):
    pass


class CreateCustomFormPayload(BaseSchema):
    pass


class EditCustomFormPayload(BaseSchema):
    pass


class EditTicketPayload(BaseSchema):
    pass


class AgentChangePayload(BaseSchema):
    pass


class CreateVideoRoomResponse(BaseSchema):
    pass


class CloseVideoRoomResponse(BaseSchema):
    pass


class CreateVideoRoomPayload(BaseSchema):
    pass


class NotifyUser(BaseSchema):
    pass


class Filter(BaseSchema):
    pass


class TicketHistoryPayload(BaseSchema):
    pass


class CustomFormSubmissionPayload(BaseSchema):
    pass


class GetTokenForVideoRoomResponse(BaseSchema):
    pass


class GetParticipantsInsideVideoRoomResponse(BaseSchema):
    pass


class Participant(BaseSchema):
    pass


class UserSchema(BaseSchema):
    pass


class PhoneNumber(BaseSchema):
    pass


class Email(BaseSchema):
    pass


class Debug(BaseSchema):
    pass


class SubmitCustomFormResponse(BaseSchema):
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


class Status(BaseSchema):
    pass


class TicketFeedbackForm(BaseSchema):
    pass


class TicketFeedbackList(BaseSchema):
    pass


class TicketFeedbackPayload(BaseSchema):
    pass


class SubmitButton(BaseSchema):
    pass


class PollForAssignment(BaseSchema):
    pass


class CustomForm(BaseSchema):
    pass


class CommunicationDetails(BaseSchema):
    pass


class SupportGeneralConfig(BaseSchema):
    pass


class FeedbackForm(BaseSchema):
    pass


class TicketSubCategory(BaseSchema):
    pass


class TicketCategory(BaseSchema):
    pass


class CategoryData(BaseSchema):
    pass


class IntegrationConfig(BaseSchema):
    pass


class FeedbackResponseItem(BaseSchema):
    pass


class TicketFeedback(BaseSchema):
    pass


class TicketHistory(BaseSchema):
    pass


class Ticket(BaseSchema):
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
    


class TicketHistoryList(BaseSchema):
    # Lead swagger.json

    
    items = fields.List(fields.Nested(TicketHistory, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CustomFormList(BaseSchema):
    # Lead swagger.json

    
    items = fields.List(fields.Nested(CustomForm, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CreateCustomFormPayload(BaseSchema):
    # Lead swagger.json

    
    slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    inputs = fields.List(fields.Dict(required=False), required=False)
    
    description = fields.Str(required=False)
    
    header_image = fields.Str(required=False)
    
    priority = fields.Nested(PriorityEnum, required=False)
    
    should_notify = fields.Boolean(required=False)
    
    success_message = fields.Str(required=False)
    
    poll_for_assignment = fields.Nested(PollForAssignment, required=False)
    


class EditCustomFormPayload(BaseSchema):
    # Lead swagger.json

    
    title = fields.Str(required=False)
    
    inputs = fields.List(fields.Dict(required=False), required=False)
    
    description = fields.Str(required=False)
    
    priority = fields.Nested(PriorityEnum, required=False)
    
    header_image = fields.Str(required=False)
    
    should_notify = fields.Boolean(required=False)
    
    login_required = fields.Boolean(required=False)
    
    success_message = fields.Str(required=False)
    
    poll_for_assignment = fields.Nested(PollForAssignment, required=False)
    


class EditTicketPayload(BaseSchema):
    # Lead swagger.json

    
    content = fields.Nested(TicketContent, required=False)
    
    category = fields.Str(required=False)
    
    sub_category = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    priority = fields.Nested(PriorityEnum, required=False)
    
    assigned_to = fields.Nested(AgentChangePayload, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class AgentChangePayload(BaseSchema):
    # Lead swagger.json

    
    agent_id = fields.Str(required=False)
    


class CreateVideoRoomResponse(BaseSchema):
    # Lead swagger.json

    
    unique_name = fields.Str(required=False)
    


class CloseVideoRoomResponse(BaseSchema):
    # Lead swagger.json

    
    success = fields.Boolean(required=False)
    


class CreateVideoRoomPayload(BaseSchema):
    # Lead swagger.json

    
    unique_name = fields.Str(required=False)
    
    notify = fields.List(fields.Nested(NotifyUser, required=False), required=False)
    


class NotifyUser(BaseSchema):
    # Lead swagger.json

    
    country_code = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    


class Filter(BaseSchema):
    # Lead swagger.json

    
    priorities = fields.List(fields.Nested(Priority, required=False), required=False)
    
    categories = fields.List(fields.Nested(TicketCategory, required=False), required=False)
    
    statuses = fields.List(fields.Nested(Status, required=False), required=False)
    
    assignees = fields.List(fields.Dict(required=False), required=False)
    


class TicketHistoryPayload(BaseSchema):
    # Lead swagger.json

    
    value = fields.Dict(required=False)
    
    type = fields.Nested(HistoryTypeEnum, required=False)
    


class CustomFormSubmissionPayload(BaseSchema):
    # Lead swagger.json

    
    response = fields.List(fields.Dict(required=False), required=False)
    
    attachments = fields.List(fields.Nested(TicketAsset, required=False), required=False)
    


class GetTokenForVideoRoomResponse(BaseSchema):
    # Lead swagger.json

    
    access_token = fields.Str(required=False)
    


class GetParticipantsInsideVideoRoomResponse(BaseSchema):
    # Lead swagger.json

    
    participants = fields.List(fields.Nested(Participant, required=False), required=False)
    


class Participant(BaseSchema):
    # Lead swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    identity = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class UserSchema(BaseSchema):
    # Lead swagger.json

    
    application_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    last_name = fields.Str(required=False)
    
    phone_numbers = fields.List(fields.Nested(PhoneNumber, required=False), required=False)
    
    emails = fields.List(fields.Nested(Email, required=False), required=False)
    
    gender = fields.Str(required=False)
    
    dob = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    profile_pic_url = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    account_type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class PhoneNumber(BaseSchema):
    # Lead swagger.json

    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    phone = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class Email(BaseSchema):
    # Lead swagger.json

    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    


class Debug(BaseSchema):
    # Lead swagger.json

    
    source = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    


class SubmitCustomFormResponse(BaseSchema):
    # Lead swagger.json

    
    message = fields.Str(required=False)
    
    ticket = fields.Nested(Ticket, required=False)
    


class TicketContext(BaseSchema):
    # Lead swagger.json

    
    application_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    


class CreatedOn(BaseSchema):
    # Lead swagger.json

    
    user_agent = fields.Str(required=False)
    


class TicketAsset(BaseSchema):
    # Lead swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Nested(TicketAssetTypeEnum, required=False)
    


class TicketContent(BaseSchema):
    # Lead swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    attachments = fields.List(fields.Nested(TicketAsset, required=False), required=False)
    


class AddTicketPayload(BaseSchema):
    # Lead swagger.json

    
    created_by = fields.Dict(required=False)
    
    status = fields.Str(required=False)
    
    priority = fields.Nested(PriorityEnum, required=False)
    
    category = fields.Str(required=False)
    
    content = fields.Nested(TicketContent, required=False)
    
    _custom_json = fields.Dict(required=False)
    


class Priority(BaseSchema):
    # Lead swagger.json

    
    key = fields.Nested(PriorityEnum, required=False)
    
    display = fields.Str(required=False)
    
    color = fields.Str(required=False)
    


class Status(BaseSchema):
    # Lead swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    color = fields.Str(required=False)
    


class TicketFeedbackForm(BaseSchema):
    # Lead swagger.json

    
    title = fields.Str(required=False)
    
    display = fields.List(fields.Dict(required=False), required=False)
    


class TicketFeedbackList(BaseSchema):
    # Lead swagger.json

    
    items = fields.List(fields.Nested(TicketFeedback, required=False), required=False)
    


class TicketFeedbackPayload(BaseSchema):
    # Lead swagger.json

    
    form_response = fields.Dict(required=False)
    


class SubmitButton(BaseSchema):
    # Lead swagger.json

    
    title = fields.Str(required=False)
    
    title_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    


class PollForAssignment(BaseSchema):
    # Lead swagger.json

    
    duration = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    success_message = fields.Str(required=False)
    
    failure_message = fields.Str(required=False)
    


class CustomForm(BaseSchema):
    # Lead swagger.json

    
    application_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    header_image = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    priority = fields.Nested(Priority, required=False)
    
    login_required = fields.Boolean(required=False)
    
    should_notify = fields.Boolean(required=False)
    
    success_message = fields.Str(required=False)
    
    submit_button = fields.Nested(SubmitButton, required=False)
    
    inputs = fields.List(fields.Dict(required=False), required=False)
    
    created_on = fields.Nested(CreatedOn, required=False)
    
    poll_for_assignment = fields.Nested(PollForAssignment, required=False)
    
    _id = fields.Str(required=False)
    


class CommunicationDetails(BaseSchema):
    # Lead swagger.json

    
    type = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    


class SupportGeneralConfig(BaseSchema):
    # Lead swagger.json

    
    _id = fields.Str(required=False)
    
    support_email = fields.Nested(CommunicationDetails, required=False)
    
    support_phone = fields.Nested(CommunicationDetails, required=False)
    
    support_faq = fields.Nested(CommunicationDetails, required=False)
    
    show_communication_info = fields.Boolean(required=False)
    
    support_communication = fields.Nested(CommunicationDetails, required=False)
    
    show_support_dris = fields.Boolean(required=False)
    
    integration = fields.Dict(required=False)
    


class FeedbackForm(BaseSchema):
    # Lead swagger.json

    
    inputs = fields.Dict(required=False)
    
    title = fields.Str(required=False)
    
    timestamps = fields.Dict(required=False)
    


class TicketSubCategory(BaseSchema):
    # Lead swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    sub_categories = fields.Nested(lambda: TicketSubCategory(exclude=('sub_categories')), required=False)
    


class TicketCategory(BaseSchema):
    # Lead swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    sub_categories = fields.Nested(lambda: TicketCategory(exclude=('sub_categories')), required=False)
    
    group_id = fields.Float(required=False)
    
    feedback_form = fields.Nested(FeedbackForm, required=False)
    


class CategoryData(BaseSchema):
    # Lead swagger.json

    
    list = fields.Nested(TicketCategory, required=False)
    


class IntegrationConfig(BaseSchema):
    # Lead swagger.json

    
    _id = fields.Str(required=False)
    
    integration_type = fields.Str(required=False)
    
    base_url = fields.Str(required=False)
    
    create_ticket_apikey = fields.Str(required=False)
    
    update_ticket_apikey = fields.Str(required=False)
    
    category_sync_apikey = fields.Str(required=False)
    
    category_data = fields.Nested(CategoryData, required=False)
    
    webhook_apikey = fields.Str(required=False)
    
    config_completed = fields.Boolean(required=False)
    
    allow_ticket_creation = fields.Boolean(required=False)
    
    show_listing = fields.Boolean(required=False)
    


class FeedbackResponseItem(BaseSchema):
    # Lead swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class TicketFeedback(BaseSchema):
    # Lead swagger.json

    
    _id = fields.Str(required=False)
    
    ticket_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    response = fields.List(fields.Nested(FeedbackResponseItem, required=False), required=False)
    
    category = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    


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
    


class Ticket(BaseSchema):
    # Lead swagger.json

    
    context = fields.Nested(TicketContext, required=False)
    
    created_on = fields.Nested(CreatedOn, required=False)
    
    response_id = fields.Str(required=False)
    
    content = fields.Nested(TicketContent, required=False)
    
    category = fields.Nested(TicketCategory, required=False)
    
    sub_category = fields.Str(required=False)
    
    source = fields.Nested(TicketSourceEnum, required=False)
    
    status = fields.Nested(Status, required=False)
    
    priority = fields.Nested(Priority, required=False)
    
    created_by = fields.Dict(required=False)
    
    assigned_to = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_feedback_pending = fields.Boolean(required=False)
    
    integration = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    


