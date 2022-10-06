"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .SendOtpSmsCommsTemplate import SendOtpSmsCommsTemplate


class SendOtpCommsReqSms(BaseSchema):
    # Communication swagger.json

    
    otp_length = fields.Int(required=False)
    
    expiry = fields.Int(required=False)
    
    template = fields.Nested(SendOtpSmsCommsTemplate, required=False)
    

