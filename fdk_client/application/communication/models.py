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


class PushtokenReq(BaseSchema):
    pass


class PushtokenRes(BaseSchema):
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
    
    encrypted = fields.Boolean(required=False)
    


class CommunicationConsentChannelsEmail(BaseSchema):
    # Communication swagger.json

    
    response = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CommunicationConsentChannelsSms(BaseSchema):
    # Communication swagger.json

    
    response = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CommunicationConsentChannelsWhatsapp(BaseSchema):
    # Communication swagger.json

    
    response = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


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
    


