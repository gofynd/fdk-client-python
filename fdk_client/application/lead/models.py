"""Lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema


from .enums import *



class TicketHistoryPayload(BaseSchema):
    pass


class CustomFormSubmissionPayload(BaseSchema):
    pass


class UserSchema(BaseSchema):
    pass


class SubmitCustomFormResponse(BaseSchema):
    pass


class FormResponse(BaseSchema):
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


class SubmitButton(BaseSchema):
    pass


class PollForAssignment(BaseSchema):
    pass


class CustomForm(BaseSchema):
    pass


class FeedbackForm(BaseSchema):
    pass


class TicketCategory(BaseSchema):
    pass


class TicketHistory(BaseSchema):
    pass


class Ticket(BaseSchema):
    pass


class NotFoundError(BaseSchema):
    pass


class Error4XX(BaseSchema):
    pass


class PhoneNumber(BaseSchema):
    pass


class Email(BaseSchema):
    pass





class TicketHistoryPayload(BaseSchema):
    # Lead swagger.json

    
    value = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    


class CustomFormSubmissionPayload(BaseSchema):
    # Lead swagger.json

    
    response = fields.List(fields.Dict(required=False), required=False)
    
    attachments = fields.List(fields.Nested(TicketAsset, required=False), required=False)
    


class UserSchema(BaseSchema):
    # Lead swagger.json

    
    application_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    last_name = fields.Str(required=False)
    
    phone_numbers = fields.List(fields.Nested(PhoneNumber, required=False), required=False)
    
    emails = fields.List(fields.Nested(Email, required=False), required=False)
    
    gender = fields.Str(required=False, allow_none=True)
    
    dob = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    profile_pic_url = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    account_type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    external_id = fields.Str(required=False)
    
    rr_id = fields.Str(required=False)
    


class SubmitCustomFormResponse(BaseSchema):
    # Lead swagger.json

    
    message = fields.Str(required=False)
    
    ticket = fields.Nested(Ticket, required=False)
    
    notified_to = fields.List(fields.Str(required=False), required=False)
    
    response = fields.Nested(FormResponse, required=False)
    


class FormResponse(BaseSchema):
    # Lead swagger.json

    
    application_id = fields.Str(required=False)
    
    form_slug = fields.Str(required=False)
    
    response = fields.List(fields.Dict(required=False), required=False)
    
    created_by = fields.Str(required=False)
    
    created_on = fields.Nested(CreatedOn, required=False)
    
    _id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    


class TicketContext(BaseSchema):
    # Lead swagger.json

    
    application_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    


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
    
    subscribers = fields.List(fields.Str(required=False), required=False)
    


class Priority(BaseSchema):
    # Lead swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    color = fields.Str(required=False)
    


class Status(BaseSchema):
    # Lead swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    color = fields.Str(required=False)
    


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
    
    login_required = fields.Boolean(required=False)
    
    should_notify = fields.Boolean(required=False)
    
    success_message = fields.Str(required=False)
    
    submit_button = fields.Nested(SubmitButton, required=False)
    
    inputs = fields.List(fields.Dict(required=False), required=False)
    
    created_on = fields.Nested(CreatedOn, required=False)
    
    poll_for_assignment = fields.Nested(PollForAssignment, required=False)
    
    available_assignees = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    
    created_by = fields.Str(required=False)
    


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
    
    created_by = fields.Str(required=False)
    
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
    
    source = fields.Str(required=False, validate=OneOf([val.value for val in TicketSourceEnum.__members__.values()]))
    
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
    
    video_room_id = fields.Str(required=False)
    
    subscribers = fields.List(fields.Str(required=False), required=False)
    
    additional_info = fields.List(fields.Dict(required=False), required=False)
    
    __v = fields.Float(required=False)
    
    attachments = fields.List(fields.Nested(TicketAsset, required=False), required=False)
    


class NotFoundError(BaseSchema):
    # Lead swagger.json

    
    message = fields.Str(required=False)
    


class Error4XX(BaseSchema):
    # Lead swagger.json

    
    message = fields.Dict(required=False)
    
    stack = fields.Str(required=False)
    
    sentry = fields.Str(required=False)
    


class PhoneNumber(BaseSchema):
    # Lead swagger.json

    
    phone = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    


class Email(BaseSchema):
    # Lead swagger.json

    
    email = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    


