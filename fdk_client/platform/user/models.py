"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class BlockUserRequestSchema(BaseSchema):
    pass


class ArchiveUserRequestSchema(BaseSchema):
    pass


class UnDeleteUserRequestSchema(BaseSchema):
    pass


class BlockUserSuccess(BaseSchema):
    pass


class ArchiveUserSuccess(BaseSchema):
    pass


class UnDeleteUserSuccess(BaseSchema):
    pass


class UserSearchResponseSchema(BaseSchema):
    pass


class CustomerListResponseSchema(BaseSchema):
    pass


class PaginationSchema(BaseSchema):
    pass


class SessionListResponseSchema(BaseSchema):
    pass


class SessionDeleteResponseSchema(BaseSchema):
    pass


class AuthenticationApiErrorSchema(BaseSchema):
    pass


class SessionListResponseInfo(BaseSchema):
    pass


class UserGroupResponseSchema(BaseSchema):
    pass


class UserGroupListResponseSchema(BaseSchema):
    pass


class CreateUserGroupSchema(BaseSchema):
    pass


class CreateUserRequestSchema(BaseSchema):
    pass


class CreateUserResponseSchema(BaseSchema):
    pass


class CreateUserSessionRequestSchema(BaseSchema):
    pass


class CreateUserSessionResponseSchema(BaseSchema):
    pass


class PlatformSchema(BaseSchema):
    pass


class LookAndFeel(BaseSchema):
    pass


class Login(BaseSchema):
    pass


class MetaSchema(BaseSchema):
    pass


class Social(BaseSchema):
    pass


class RequiredFields(BaseSchema):
    pass


class PlatformEmail(BaseSchema):
    pass


class PlatformMobile(BaseSchema):
    pass


class RegisterRequiredFields(BaseSchema):
    pass


class RegisterRequiredFieldsEmail(BaseSchema):
    pass


class RegisterRequiredFieldsMobile(BaseSchema):
    pass


class FlashCard(BaseSchema):
    pass


class SocialTokens(BaseSchema):
    pass


class DeleteAccountReasons(BaseSchema):
    pass


class DeleteAccountConsent(BaseSchema):
    pass


class Facebook(BaseSchema):
    pass


class Accountkit(BaseSchema):
    pass


class Google(BaseSchema):
    pass


class SessionExpiry(BaseSchema):
    pass


class UpdateUserGroupSchema(BaseSchema):
    pass


class PartialUserGroupUpdateSchema(BaseSchema):
    pass


class UserGroupUpdateData(BaseSchema):
    pass


class UpdateUserRequestSchema(BaseSchema):
    pass


class UserEmails(BaseSchema):
    pass


class UserPhoneNumbers(BaseSchema):
    pass


class UserSchema(BaseSchema):
    pass


class PhoneNumber(BaseSchema):
    pass


class Email(BaseSchema):
    pass





class BlockUserRequestSchema(BaseSchema):
    # User swagger.json

    
    status = fields.Boolean(required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    reason = fields.Str(required=False)
    


class ArchiveUserRequestSchema(BaseSchema):
    # User swagger.json

    
    user_id = fields.Str(required=False)
    


class UnDeleteUserRequestSchema(BaseSchema):
    # User swagger.json

    
    user_id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    reason_id = fields.Str(required=False)
    


class BlockUserSuccess(BaseSchema):
    # User swagger.json

    
    success = fields.Boolean(required=False)
    


class ArchiveUserSuccess(BaseSchema):
    # User swagger.json

    
    success = fields.Boolean(required=False)
    


class UnDeleteUserSuccess(BaseSchema):
    # User swagger.json

    
    success = fields.Boolean(required=False)
    


class UserSearchResponseSchema(BaseSchema):
    # User swagger.json

    
    users = fields.List(fields.Nested(UserSchema, required=False), required=False)
    


class CustomerListResponseSchema(BaseSchema):
    # User swagger.json

    
    items = fields.List(fields.Nested(UserSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    


class PaginationSchema(BaseSchema):
    # User swagger.json

    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    


class SessionListResponseSchema(BaseSchema):
    # User swagger.json

    
    items = fields.List(fields.Nested(SessionListResponseInfo, required=False), required=False)
    


class SessionDeleteResponseSchema(BaseSchema):
    # User swagger.json

    
    items = fields.List(fields.Str(required=False), required=False)
    


class AuthenticationApiErrorSchema(BaseSchema):
    # User swagger.json

    
    message = fields.Str(required=False)
    


class SessionListResponseInfo(BaseSchema):
    # User swagger.json

    
    session_id = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    ip = fields.Str(required=False)
    
    domain = fields.Str(required=False)
    
    expire_in = fields.Str(required=False)
    


class UserGroupResponseSchema(BaseSchema):
    # User swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class UserGroupListResponseSchema(BaseSchema):
    # User swagger.json

    
    items = fields.List(fields.Nested(UserGroupResponseSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    


class CreateUserGroupSchema(BaseSchema):
    # User swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    


class CreateUserRequestSchema(BaseSchema):
    # User swagger.json

    
    phone_number = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    external_id = fields.Str(required=False)
    


class CreateUserResponseSchema(BaseSchema):
    # User swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    


class CreateUserSessionRequestSchema(BaseSchema):
    # User swagger.json

    
    domain = fields.Str(required=False)
    
    max_age = fields.Float(required=False)
    
    user_id = fields.Str(required=False)
    


class CreateUserSessionResponseSchema(BaseSchema):
    # User swagger.json

    
    domain = fields.Str(required=False)
    
    max_age = fields.Float(required=False)
    
    secure = fields.Boolean(required=False)
    
    http_only = fields.Boolean(required=False)
    
    cookie = fields.Dict(required=False)
    


class PlatformSchema(BaseSchema):
    # User swagger.json

    
    display = fields.Str(required=False)
    
    look_and_feel = fields.Nested(LookAndFeel, required=False)
    
    updated_at = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    forgot_password = fields.Boolean(required=False)
    
    login = fields.Nested(Login, required=False)
    
    skip_captcha = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Nested(MetaSchema, required=False)
    
    _id = fields.Str(required=False)
    
    social = fields.Nested(Social, required=False)
    
    required_fields = fields.Nested(RequiredFields, required=False)
    
    register_required_fields = fields.Nested(RegisterRequiredFields, required=False)
    
    skip_login = fields.Boolean(required=False)
    
    flash_card = fields.Nested(FlashCard, required=False)
    
    subtext = fields.Str(required=False)
    
    social_tokens = fields.Nested(SocialTokens, required=False)
    
    created_at = fields.Str(required=False)
    
    register = fields.Boolean(required=False)
    
    mobile_image = fields.Str(required=False)
    
    desktop_image = fields.Str(required=False)
    
    delete_account_day = fields.Int(required=False)
    
    delete_account_reasons = fields.List(fields.Nested(DeleteAccountReasons, required=False), required=False)
    
    delete_account_consent = fields.Dict(required=False)
    
    session_config = fields.Dict(required=False)
    


class LookAndFeel(BaseSchema):
    # User swagger.json

    
    card_position = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    


class Login(BaseSchema):
    # User swagger.json

    
    password = fields.Boolean(required=False)
    
    otp = fields.Boolean(required=False)
    


class MetaSchema(BaseSchema):
    # User swagger.json

    
    fynd_default = fields.Boolean(required=False)
    


class Social(BaseSchema):
    # User swagger.json

    
    account_kit = fields.Boolean(required=False)
    
    facebook = fields.Boolean(required=False)
    
    google = fields.Boolean(required=False)
    
    apple = fields.Boolean(required=False)
    


class RequiredFields(BaseSchema):
    # User swagger.json

    
    email = fields.Nested(PlatformEmail, required=False)
    
    mobile = fields.Nested(PlatformMobile, required=False)
    


class PlatformEmail(BaseSchema):
    # User swagger.json

    
    is_required = fields.Boolean(required=False)
    
    level = fields.Str(required=False)
    


class PlatformMobile(BaseSchema):
    # User swagger.json

    
    is_required = fields.Boolean(required=False)
    
    level = fields.Str(required=False)
    


class RegisterRequiredFields(BaseSchema):
    # User swagger.json

    
    email = fields.Nested(RegisterRequiredFieldsEmail, required=False)
    
    mobile = fields.Nested(RegisterRequiredFieldsMobile, required=False)
    


class RegisterRequiredFieldsEmail(BaseSchema):
    # User swagger.json

    
    is_required = fields.Boolean(required=False)
    
    level = fields.Str(required=False)
    


class RegisterRequiredFieldsMobile(BaseSchema):
    # User swagger.json

    
    is_required = fields.Boolean(required=False)
    
    level = fields.Str(required=False)
    


class FlashCard(BaseSchema):
    # User swagger.json

    
    text = fields.Str(required=False)
    
    text_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    


class SocialTokens(BaseSchema):
    # User swagger.json

    
    facebook = fields.Nested(Facebook, required=False)
    
    account_kit = fields.Nested(Accountkit, required=False)
    
    google = fields.Nested(Google, required=False)
    


class DeleteAccountReasons(BaseSchema):
    # User swagger.json

    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Str(required=False)
    
    show_text_area = fields.Boolean(required=False)
    


class DeleteAccountConsent(BaseSchema):
    # User swagger.json

    
    consent_text = fields.Str(required=False)
    


class Facebook(BaseSchema):
    # User swagger.json

    
    app_id = fields.Str(required=False)
    


class Accountkit(BaseSchema):
    # User swagger.json

    
    app_id = fields.Str(required=False)
    


class Google(BaseSchema):
    # User swagger.json

    
    app_id = fields.Str(required=False)
    


class SessionExpiry(BaseSchema):
    # User swagger.json

    
    duration = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    is_rolling = fields.Boolean(required=False)
    


class UpdateUserGroupSchema(BaseSchema):
    # User swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    


class PartialUserGroupUpdateSchema(BaseSchema):
    # User swagger.json

    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    user_data = fields.List(fields.Nested(UserGroupUpdateData, required=False), required=False)
    


class UserGroupUpdateData(BaseSchema):
    # User swagger.json

    
    user_id = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    action = fields.Str(required=False)
    


class UpdateUserRequestSchema(BaseSchema):
    # User swagger.json

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    external_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    phone_numbers = fields.List(fields.Nested(UserPhoneNumbers, required=False), required=False)
    
    emails = fields.List(fields.Nested(UserEmails, required=False), required=False)
    


class UserEmails(BaseSchema):
    # User swagger.json

    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    


class UserPhoneNumbers(BaseSchema):
    # User swagger.json

    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    phone = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class UserSchema(BaseSchema):
    # User swagger.json

    
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
    
    external_id = fields.Str(required=False)
    


class PhoneNumber(BaseSchema):
    # User swagger.json

    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    phone = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class Email(BaseSchema):
    # User swagger.json

    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    


