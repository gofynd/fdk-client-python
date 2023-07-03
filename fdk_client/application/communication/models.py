"""Communication Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class CommunicationConsentReq(BaseSchema):
    pass


class CommunicationConsentRes(BaseSchema):
    pass


class CommunicationConsentChannelsEmail(BaseSchema):
    pass


class CommunicationConsentChannelsSms(BaseSchema):
    pass


class CommunicationConsentChannelsWhatsapp(BaseSchema):
    pass


class CommunicationConsentChannels(BaseSchema):
    pass


class CommunicationConsent(BaseSchema):
    pass


class BadRequestSchema(BaseSchema):
    pass


class NotFound(BaseSchema):
    pass


class PushtokenReq(BaseSchema):
    pass


class PushtokenRes(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class GenericPage(BaseSchema):
    pass


class GenericSuccess(BaseSchema):
    pass


class GenericError(BaseSchema):
    pass


class GenericDelete(BaseSchema):
    pass


class Message(BaseSchema):
    pass


class EnabledObj(BaseSchema):
    pass


class InvalidRangeErrorReqPositive(BaseSchema):
    pass


class InvalidInputRequiredByteOrHexError(BaseSchema):
    pass


class NameValidatorError(BaseSchema):
    pass


class NameValidatorErrorMessage(BaseSchema):
    pass


class ApikeyValidatorError(BaseSchema):
    pass


class ApikeyValidatorErrorMessage(BaseSchema):
    pass


class FeedidValidatorError(BaseSchema):
    pass


class FeedidValidatorErrorMessage(BaseSchema):
    pass


class UsernameValidatorError(BaseSchema):
    pass


class UsernameValidatorErrorMessage(BaseSchema):
    pass


class PasswordValidatorError(BaseSchema):
    pass


class PasswordValidatorErrorMessage(BaseSchema):
    pass


class ValidatorErrorBody(BaseSchema):
    pass


class ValidatorErrorMessageProperties(BaseSchema):
    pass


class CastToStringFail(BaseSchema):
    pass


class InvalidID(BaseSchema):
    pass





class CommunicationConsentReq(BaseSchema):
    # Communication swagger.json

    
    response = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    channel = fields.Str(required=False)
    


class CommunicationConsentRes(BaseSchema):
    # Communication swagger.json

    
    app_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    channels = fields.Nested(CommunicationConsentChannels, required=False)
    


class CommunicationConsentChannelsEmail(BaseSchema):
    # Communication swagger.json

    
    response = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class CommunicationConsentChannelsSms(BaseSchema):
    # Communication swagger.json

    
    response = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class CommunicationConsentChannelsWhatsapp(BaseSchema):
    # Communication swagger.json

    
    response = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    


class CommunicationConsentChannels(BaseSchema):
    # Communication swagger.json

    
    email = fields.Nested(CommunicationConsentChannelsEmail, required=False)
    
    sms = fields.Nested(CommunicationConsentChannelsSms, required=False)
    
    whatsapp = fields.Nested(CommunicationConsentChannelsWhatsapp, required=False)
    


class CommunicationConsent(BaseSchema):
    # Communication swagger.json

    
    app_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    channels = fields.Nested(CommunicationConsentChannels, required=False)
    


class BadRequestSchema(BaseSchema):
    # Communication swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class NotFound(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    


class PushtokenReq(BaseSchema):
    # Communication swagger.json

    
    action = fields.Str(required=False)
    
    bundle_identifier = fields.Str(required=False)
    
    push_token = fields.Str(required=False)
    
    unique_device_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class PushtokenRes(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    
    bundle_identifier = fields.Str(required=False)
    
    push_token = fields.Str(required=False)
    
    unique_device_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    expired_at = fields.Str(required=False)
    


class Page(BaseSchema):
    # Communication swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class GenericPage(BaseSchema):
    # Communication swagger.json

    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    


class GenericSuccess(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    


class GenericError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Nested(Message, required=False)
    
    sentry = fields.Str(required=False)
    


class GenericDelete(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    acknowledged = fields.Boolean(required=False)
    
    affected = fields.Int(required=False)
    
    operation = fields.Str(required=False)
    


class Message(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    info = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    


class EnabledObj(BaseSchema):
    # Communication swagger.json

    
    enabled = fields.Boolean(required=False)
    


class InvalidRangeErrorReqPositive(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    code = fields.Int(required=False)
    
    sentry = fields.Str(required=False)
    


class InvalidInputRequiredByteOrHexError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    sentry = fields.Str(required=False)
    


class NameValidatorError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Nested(NameValidatorErrorMessage, required=False)
    
    sentry = fields.Str(required=False)
    


class NameValidatorErrorMessage(BaseSchema):
    # Communication swagger.json

    
    name = fields.Nested(ValidatorErrorBody, required=False)
    


class ApikeyValidatorError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Nested(ApikeyValidatorErrorMessage, required=False)
    
    sentry = fields.Str(required=False)
    


class ApikeyValidatorErrorMessage(BaseSchema):
    # Communication swagger.json

    
    api_key = fields.Nested(ValidatorErrorBody, required=False)
    


class FeedidValidatorError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Nested(FeedidValidatorErrorMessage, required=False)
    
    sentry = fields.Str(required=False)
    


class FeedidValidatorErrorMessage(BaseSchema):
    # Communication swagger.json

    
    feedid = fields.Nested(ValidatorErrorBody, required=False)
    


class UsernameValidatorError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Nested(UsernameValidatorErrorMessage, required=False)
    
    sentry = fields.Str(required=False)
    


class UsernameValidatorErrorMessage(BaseSchema):
    # Communication swagger.json

    
    username = fields.Nested(ValidatorErrorBody, required=False)
    


class PasswordValidatorError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Nested(PasswordValidatorErrorMessage, required=False)
    
    sentry = fields.Str(required=False)
    


class PasswordValidatorErrorMessage(BaseSchema):
    # Communication swagger.json

    
    password = fields.Nested(ValidatorErrorBody, required=False)
    


class ValidatorErrorBody(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    properties = fields.Nested(ValidatorErrorMessageProperties, required=False)
    
    kind = fields.Str(required=False)
    
    path = fields.Str(required=False)
    


class ValidatorErrorMessageProperties(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    path = fields.Str(required=False)
    


class CastToStringFail(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    sentry = fields.Str(required=False)
    


class InvalidID(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    sentry = fields.Str(required=False)
    


