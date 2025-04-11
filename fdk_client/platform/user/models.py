"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class SuccessMessage(BaseSchema):
    pass


class UserAttributeDefinition(BaseSchema):
    pass


class UserAttributeDefinitionResp(BaseSchema):
    pass


class UserAttributeDefinitionValidation(BaseSchema):
    pass


class UserAttribute(BaseSchema):
    pass


class CreateUserAttributePayload(BaseSchema):
    pass


class CreateUserAttributeDefinition(BaseSchema):
    pass


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


class SessionsDeleteResponseSchema(BaseSchema):
    pass


class APIError(BaseSchema):
    pass


class SessionListResponseInfo(BaseSchema):
    pass


class Conditions(BaseSchema):
    pass


class UserResponseErrorSchema(BaseSchema):
    pass


class UserGroupResponseSchema(BaseSchema):
    pass


class UserGroupListResponseSchema(BaseSchema):
    pass


class ConditionsSchema(BaseSchema):
    pass


class CreateUserGroup(BaseSchema):
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


class PasswordConfigs(BaseSchema):
    pass


class PasswordHistory(BaseSchema):
    pass


class PasswordExpiry(BaseSchema):
    pass


class PasswordSettings(BaseSchema):
    pass


class AccountLockout(BaseSchema):
    pass


class Login(BaseSchema):
    pass


class MetaSchema(BaseSchema):
    pass


class Social(BaseSchema):
    pass


class PlatformPassword(BaseSchema):
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


class UserPasswordHistory(BaseSchema):
    pass


class UserSchema(BaseSchema):
    pass


class UserSearchSchema(BaseSchema):
    pass


class DebugInfo(BaseSchema):
    pass


class PhoneNumber(BaseSchema):
    pass


class Email(BaseSchema):
    pass





class SuccessMessage(BaseSchema):
    # User swagger.json

    
    success = fields.Str(required=False)
    


class UserAttributeDefinition(BaseSchema):
    # User swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    multi_value = fields.Boolean(required=False)
    
    customer_editable = fields.Boolean(required=False)
    
    encrypted = fields.Boolean(required=False)
    
    pinned = fields.Boolean(required=False)
    
    pin_order = fields.Int(required=False)
    
    validations = fields.List(fields.Dict(required=False), required=False)
    
    is_locked = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class UserAttributeDefinitionResp(BaseSchema):
    # User swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    multi_value = fields.Boolean(required=False)
    
    customer_editable = fields.Boolean(required=False)
    
    encrypted = fields.Boolean(required=False)
    
    pinned = fields.Boolean(required=False)
    
    pin_order = fields.Int(required=False)
    
    validations = fields.List(fields.Nested(UserAttributeDefinitionValidation, required=False), required=False)
    
    is_locked = fields.Boolean(required=False)
    
    created_by = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    


class UserAttributeDefinitionValidation(BaseSchema):
    # User swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Raw(required=False)
    


class UserAttribute(BaseSchema):
    # User swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    customer_overriden = fields.Boolean(required=False)
    
    attribute = fields.Dict(required=False)
    
    updated_by = fields.Str(required=False)
    


class CreateUserAttributePayload(BaseSchema):
    # User swagger.json

    
    customer_overriden = fields.Boolean(required=False)
    
    attribute = fields.Dict(required=False)
    


class CreateUserAttributeDefinition(BaseSchema):
    # User swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    multi_value = fields.Boolean(required=False)
    
    customer_editable = fields.Boolean(required=False)
    
    encrypted = fields.Boolean(required=False)
    
    pinned = fields.Boolean(required=False)
    
    pin_order = fields.Float(required=False)
    
    default_value = fields.Dict(required=False)
    
    validations = fields.List(fields.Dict(required=False), required=False)
    


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

    
    users = fields.List(fields.Nested(UserSearchSchema, required=False), required=False)
    


class CustomerListResponseSchema(BaseSchema):
    # User swagger.json

    
    items = fields.List(fields.Nested(UserSearchSchema, required=False), required=False)
    
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

    
    user_id = fields.Str(required=False)
    
    session_id = fields.Str(required=False)
    


class SessionsDeleteResponseSchema(BaseSchema):
    # User swagger.json

    
    user_id = fields.Str(required=False)
    
    session_ids = fields.List(fields.Str(required=False), required=False)
    


class APIError(BaseSchema):
    # User swagger.json

    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    error = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    authenticated = fields.Boolean(required=False)
    


class SessionListResponseInfo(BaseSchema):
    # User swagger.json

    
    session_id = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    ip = fields.Str(required=False)
    
    domain = fields.Str(required=False)
    
    expire_in = fields.Str(required=False)
    
    location = fields.Str(required=False)
    


class Conditions(BaseSchema):
    # User swagger.json

    
    user_attribute_definition_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    
    key = fields.Str(required=False)
    


class UserResponseErrorSchema(BaseSchema):
    # User swagger.json

    
    count = fields.Int(required=False)
    
    file_url = fields.Str(required=False)
    


class UserGroupResponseSchema(BaseSchema):
    # User swagger.json

    
    conditions = fields.List(fields.Nested(Conditions, required=False), required=False)
    
    blacklisted_users = fields.List(fields.Str(required=False), required=False)
    
    error = fields.Nested(UserResponseErrorSchema, required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class UserGroupListResponseSchema(BaseSchema):
    # User swagger.json

    
    items = fields.List(fields.Nested(UserGroupResponseSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    


class ConditionsSchema(BaseSchema):
    # User swagger.json

    
    user_attribute_definition_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    


class CreateUserGroup(BaseSchema):
    # User swagger.json

    
    conditions = fields.List(fields.Nested(ConditionsSchema, required=False), required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    blacklisted_users = fields.List(fields.Str(required=False), required=False)
    


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
    
    rr_id = fields.Str(required=False)
    


class CreateUserResponseSchema(BaseSchema):
    # User swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    


class CreateUserSessionRequestSchema(BaseSchema):
    # User swagger.json

    
    domain = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    max_age = fields.Float(required=False)
    


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
    
    account_lockout = fields.Nested(AccountLockout, required=False)
    
    password_settings = fields.Nested(PasswordSettings, required=False)
    
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
    
    mobile_image = fields.Str(required=False, allow_none=True)
    
    desktop_image = fields.Str(required=False, allow_none=True)
    
    delete_account_day = fields.Int(required=False)
    
    delete_account_reasons = fields.List(fields.Nested(DeleteAccountReasons, required=False), required=False)
    
    delete_account_consent = fields.Nested(DeleteAccountConsent, required=False)
    
    session_config = fields.Nested(SessionExpiry, required=False)
    
    __v = fields.Int(required=False)
    


class LookAndFeel(BaseSchema):
    # User swagger.json

    
    card_position = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    


class PasswordConfigs(BaseSchema):
    # User swagger.json

    
    length = fields.Float(required=False)
    
    require_special_character = fields.Boolean(required=False)
    
    require_number = fields.Boolean(required=False)
    
    require_capital_character = fields.Boolean(required=False)
    


class PasswordHistory(BaseSchema):
    # User swagger.json

    
    required = fields.Boolean(required=False)
    
    count = fields.Float(required=False)
    


class PasswordExpiry(BaseSchema):
    # User swagger.json

    
    required = fields.Boolean(required=False)
    
    duration = fields.Float(required=False)
    


class PasswordSettings(BaseSchema):
    # User swagger.json

    
    configs = fields.Nested(PasswordConfigs, required=False)
    
    history = fields.Nested(PasswordHistory, required=False)
    
    expiry = fields.Nested(PasswordExpiry, required=False)
    


class AccountLockout(BaseSchema):
    # User swagger.json

    
    enable = fields.Boolean(required=False)
    
    attempts = fields.Float(required=False)
    
    duration = fields.Float(required=False)
    


class Login(BaseSchema):
    # User swagger.json

    
    password = fields.Boolean(required=False)
    
    otp = fields.Boolean(required=False)
    
    via = fields.Str(required=False)
    


class MetaSchema(BaseSchema):
    # User swagger.json

    
    fynd_default = fields.Boolean(required=False)
    


class Social(BaseSchema):
    # User swagger.json

    
    account_kit = fields.Boolean(required=False)
    
    facebook = fields.Boolean(required=False)
    
    google = fields.Boolean(required=False)
    
    apple = fields.Boolean(required=False)
    


class PlatformPassword(BaseSchema):
    # User swagger.json

    
    is_required = fields.Boolean(required=False)
    


class RequiredFields(BaseSchema):
    # User swagger.json

    
    email = fields.Nested(PlatformEmail, required=False)
    
    mobile = fields.Nested(PlatformMobile, required=False)
    
    password = fields.Nested(PlatformPassword, required=False)
    


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
    
    password = fields.Nested(PlatformPassword, required=False)
    


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
    
    accountkit = fields.Nested(Accountkit, required=False)
    
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
    
    app_secret = fields.Str(required=False)
    


class Accountkit(BaseSchema):
    # User swagger.json

    
    app_id = fields.Str(required=False)
    
    app_secret = fields.Str(required=False)
    


class Google(BaseSchema):
    # User swagger.json

    
    app_id = fields.Str(required=False)
    
    app_secret = fields.Str(required=False)
    


class SessionExpiry(BaseSchema):
    # User swagger.json

    
    duration = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    is_rolling = fields.Boolean(required=False)
    


class UpdateUserGroupSchema(BaseSchema):
    # User swagger.json

    
    conditions = fields.List(fields.Nested(ConditionsSchema, required=False), required=False)
    
    type = fields.Str(required=False)
    
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
    
    whitelisted_users = fields.List(fields.Str(required=False), required=False)
    
    blacklisted_users = fields.List(fields.Str(required=False), required=False)
    


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
    
    rr_id = fields.Str(required=False)
    
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
    


class UserPasswordHistory(BaseSchema):
    # User swagger.json

    
    salt = fields.Str(required=False)
    
    hash = fields.Str(required=False)
    


class UserSchema(BaseSchema):
    # User swagger.json

    
    application_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    password_last_modified = fields.Str(required=False)
    
    password_history = fields.List(fields.Nested(UserPasswordHistory, required=False), required=False)
    
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
    


class UserSearchSchema(BaseSchema):
    # User swagger.json

    
    __v = fields.Float(required=False)
    
    has_old_password_hash = fields.Boolean(required=False)
    
    debug = fields.Nested(DebugInfo, required=False)
    
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
    
    archive = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    


class DebugInfo(BaseSchema):
    # User swagger.json

    
    source = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    


class PhoneNumber(BaseSchema):
    # User swagger.json

    
    phone = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    


class Email(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    


