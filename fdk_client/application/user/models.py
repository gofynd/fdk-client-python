"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class DeleteApplicationUserRequestSchema(BaseSchema):
    pass


class EditEmailRequestSchema(BaseSchema):
    pass


class SendVerificationLinkMobileRequestSchema(BaseSchema):
    pass


class EditMobileRequestSchema(BaseSchema):
    pass


class EditProfileRequestSchema(BaseSchema):
    pass


class EditProfileMobileSchema(BaseSchema):
    pass


class SendEmailOtpRequestSchema(BaseSchema):
    pass


class SendEmailForgotOtpRequestSchema(BaseSchema):
    pass


class VerifyEmailOtpRequestSchema(BaseSchema):
    pass


class VerifyEmailForgotOtpRequestSchema(BaseSchema):
    pass


class VerifyOtpRequestSchema(BaseSchema):
    pass


class VerifyMobileForgotOtpRequestSchema(BaseSchema):
    pass


class SendMobileOtpRequestSchema(BaseSchema):
    pass


class SendMobileForgotOtpRequestSchema(BaseSchema):
    pass


class UpdatePasswordRequestSchema(BaseSchema):
    pass


class FormRegisterRequestSchema(BaseSchema):
    pass


class TokenRequestBodySchema(BaseSchema):
    pass


class ForgotPasswordRequestSchema(BaseSchema):
    pass


class CodeRequestBodySchema(BaseSchema):
    pass


class SendResetPasswordEmailRequestSchema(BaseSchema):
    pass


class SendResetPasswordMobileRequestSchema(BaseSchema):
    pass


class PasswordLoginRequestSchema(BaseSchema):
    pass


class SendOtpRequestSchema(BaseSchema):
    pass


class OAuthRequestSchema(BaseSchema):
    pass


class OAuthRequestAppleSchema(BaseSchema):
    pass


class UserObjectSchema(BaseSchema):
    pass


class AuthSuccess(BaseSchema):
    pass


class SendOtpResponse(BaseSchema):
    pass


class ProfileEditSuccess(BaseSchema):
    pass


class LoginSuccess(BaseSchema):
    pass


class ResetForgotPasswordSuccess(BaseSchema):
    pass


class VerifyOtpSuccess(BaseSchema):
    pass


class VerifyForgotOtpSuccess(BaseSchema):
    pass


class ResetPasswordSuccess(BaseSchema):
    pass


class RegisterFormSuccess(BaseSchema):
    pass


class VerifyEmailSuccess(BaseSchema):
    pass


class HasPasswordSuccess(BaseSchema):
    pass


class LogoutSuccess(BaseSchema):
    pass


class DeleteUserSuccess(BaseSchema):
    pass


class OtpSuccess(BaseSchema):
    pass


class EmailOtpSuccess(BaseSchema):
    pass


class SessionListSuccess(BaseSchema):
    pass


class VerifyMobileOTPSuccess(BaseSchema):
    pass


class VerifyEmailOTPSuccess(BaseSchema):
    pass


class SendMobileVerifyLinkSuccess(BaseSchema):
    pass


class SendEmailVerifyLinkSuccess(BaseSchema):
    pass


class AuthenticationInternalServerErrorSchema(BaseSchema):
    pass


class AuthenticationApiErrorSchema(BaseSchema):
    pass


class APIError(BaseSchema):
    pass


class FormRegisterRequestSchemaPhone(BaseSchema):
    pass


class OAuthRequestSchemaOauth2(BaseSchema):
    pass


class OAuthRequestSchemaProfile(BaseSchema):
    pass


class OAuthRequestAppleSchemaOauth(BaseSchema):
    pass


class OAuthRequestAppleSchemaProfile(BaseSchema):
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


class UserSchema(BaseSchema):
    pass


class PhoneNumber(BaseSchema):
    pass


class Email(BaseSchema):
    pass





class DeleteApplicationUserRequestSchema(BaseSchema):
    # User swagger.json

    
    user_id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    reason_id = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    


class EditEmailRequestSchema(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    


class SendVerificationLinkMobileRequestSchema(BaseSchema):
    # User swagger.json

    
    verified = fields.Boolean(required=False)
    
    active = fields.Boolean(required=False)
    
    country_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    primary = fields.Boolean(required=False)
    


class EditMobileRequestSchema(BaseSchema):
    # User swagger.json

    
    country_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    


class EditProfileRequestSchema(BaseSchema):
    # User swagger.json

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    mobile = fields.Nested(EditProfileMobileSchema, required=False)
    
    country_code = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    dob = fields.Str(required=False)
    
    profile_pic_url = fields.Str(required=False)
    
    android_hash = fields.Str(required=False)
    
    sender = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    


class EditProfileMobileSchema(BaseSchema):
    # User swagger.json

    
    phone = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class SendEmailOtpRequestSchema(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    


class SendEmailForgotOtpRequestSchema(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    token = fields.Str(required=False)
    


class VerifyEmailOtpRequestSchema(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    


class VerifyEmailForgotOtpRequestSchema(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    


class VerifyOtpRequestSchema(BaseSchema):
    # User swagger.json

    
    request_id = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    


class VerifyMobileForgotOtpRequestSchema(BaseSchema):
    # User swagger.json

    
    request_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    


class SendMobileOtpRequestSchema(BaseSchema):
    # User swagger.json

    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    android_hash = fields.Str(required=False)
    
    force = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    


class SendMobileForgotOtpRequestSchema(BaseSchema):
    # User swagger.json

    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    android_hash = fields.Str(required=False)
    


class UpdatePasswordRequestSchema(BaseSchema):
    # User swagger.json

    
    old_password = fields.Str(required=False)
    
    new_password = fields.Str(required=False)
    


class FormRegisterRequestSchema(BaseSchema):
    # User swagger.json

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    phone = fields.Nested(FormRegisterRequestSchemaPhone, required=False)
    
    register_token = fields.Str(required=False)
    


class TokenRequestBodySchema(BaseSchema):
    # User swagger.json

    
    token = fields.Str(required=False)
    


class ForgotPasswordRequestSchema(BaseSchema):
    # User swagger.json

    
    code = fields.Str(required=False)
    
    password = fields.Str(required=False)
    


class CodeRequestBodySchema(BaseSchema):
    # User swagger.json

    
    code = fields.Str(required=False)
    


class SendResetPasswordEmailRequestSchema(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    


class SendResetPasswordMobileRequestSchema(BaseSchema):
    # User swagger.json

    
    country_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    


class PasswordLoginRequestSchema(BaseSchema):
    # User swagger.json

    
    captcha_code = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class SendOtpRequestSchema(BaseSchema):
    # User swagger.json

    
    country_code = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    android_hash = fields.Str(required=False)
    


class OAuthRequestSchema(BaseSchema):
    # User swagger.json

    
    is_signed_in = fields.Boolean(required=False)
    
    oauth2 = fields.Nested(OAuthRequestSchemaOauth2, required=False)
    
    profile = fields.Nested(OAuthRequestSchemaProfile, required=False)
    


class OAuthRequestAppleSchema(BaseSchema):
    # User swagger.json

    
    user_identifier = fields.Str(required=False)
    
    oauth = fields.Nested(OAuthRequestAppleSchemaOauth, required=False)
    
    profile = fields.Nested(OAuthRequestAppleSchemaProfile, required=False)
    


class UserObjectSchema(BaseSchema):
    # User swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    


class AuthSuccess(BaseSchema):
    # User swagger.json

    
    register_token = fields.Str(required=False)
    
    user_exists = fields.Boolean(required=False)
    
    user = fields.Nested(UserSchema, required=False)
    


class SendOtpResponse(BaseSchema):
    # User swagger.json

    
    resend_timer = fields.Int(required=False)
    
    resend_token = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    resend_email_token = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    verify_email_otp = fields.Boolean(required=False)
    
    verify_mobile_otp = fields.Boolean(required=False)
    
    user_exists = fields.Boolean(required=False)
    


class ProfileEditSuccess(BaseSchema):
    # User swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    register_token = fields.Str(required=False)
    
    resend_email_token = fields.Str(required=False)
    
    user_exists = fields.Boolean(required=False)
    
    verify_email_link = fields.Boolean(required=False)
    
    verify_email_otp = fields.Boolean(required=False)
    
    verify_mobile_otp = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    
    resend_token = fields.Str(required=False)
    


class LoginSuccess(BaseSchema):
    # User swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    request_id = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    


class ResetForgotPasswordSuccess(BaseSchema):
    # User swagger.json

    
    success = fields.Boolean(required=False)
    


class VerifyOtpSuccess(BaseSchema):
    # User swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    user_exists = fields.Boolean(required=False)
    
    register_token = fields.Str(required=False)
    


class VerifyForgotOtpSuccess(BaseSchema):
    # User swagger.json

    
    success = fields.Boolean(required=False)
    
    forgot_token = fields.Str(required=False)
    


class ResetPasswordSuccess(BaseSchema):
    # User swagger.json

    
    status = fields.Str(required=False)
    


class RegisterFormSuccess(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    
    resend_token = fields.Str(required=False)
    
    resend_email_token = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    verify_email_otp = fields.Boolean(required=False)
    
    verify_mobile_otp = fields.Boolean(required=False)
    
    user_exists = fields.Boolean(required=False)
    


class VerifyEmailSuccess(BaseSchema):
    # User swagger.json

    
    message = fields.Str(required=False)
    


class HasPasswordSuccess(BaseSchema):
    # User swagger.json

    
    result = fields.Boolean(required=False)
    


class LogoutSuccess(BaseSchema):
    # User swagger.json

    
    logout = fields.Boolean(required=False)
    


class DeleteUserSuccess(BaseSchema):
    # User swagger.json

    
    success = fields.Boolean(required=False)
    


class OtpSuccess(BaseSchema):
    # User swagger.json

    
    resend_timer = fields.Int(required=False)
    
    resend_token = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class EmailOtpSuccess(BaseSchema):
    # User swagger.json

    
    success = fields.Boolean(required=False)
    


class SessionListSuccess(BaseSchema):
    # User swagger.json

    
    sessions = fields.List(fields.Str(required=False), required=False)
    


class VerifyMobileOTPSuccess(BaseSchema):
    # User swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    verify_mobile_link = fields.Boolean(required=False)
    


class VerifyEmailOTPSuccess(BaseSchema):
    # User swagger.json

    
    user = fields.Nested(UserSchema, required=False)
    
    verify_email_link = fields.Boolean(required=False)
    


class SendMobileVerifyLinkSuccess(BaseSchema):
    # User swagger.json

    
    verify_mobile_link = fields.Boolean(required=False)
    


class SendEmailVerifyLinkSuccess(BaseSchema):
    # User swagger.json

    
    verify_email_link = fields.Boolean(required=False)
    


class AuthenticationInternalServerErrorSchema(BaseSchema):
    # User swagger.json

    
    message = fields.Str(required=False)
    


class AuthenticationApiErrorSchema(BaseSchema):
    # User swagger.json

    
    message = fields.Str(required=False)
    


class APIError(BaseSchema):
    # User swagger.json

    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class FormRegisterRequestSchemaPhone(BaseSchema):
    # User swagger.json

    
    country_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class OAuthRequestSchemaOauth2(BaseSchema):
    # User swagger.json

    
    access_token = fields.Str(required=False)
    
    expiry = fields.Int(required=False)
    
    refresh_token = fields.Str(required=False)
    


class OAuthRequestSchemaProfile(BaseSchema):
    # User swagger.json

    
    last_name = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    full_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    


class OAuthRequestAppleSchemaOauth(BaseSchema):
    # User swagger.json

    
    identity_token = fields.Str(required=False)
    


class OAuthRequestAppleSchemaProfile(BaseSchema):
    # User swagger.json

    
    last_name = fields.Str(required=False)
    
    full_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    


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
    


