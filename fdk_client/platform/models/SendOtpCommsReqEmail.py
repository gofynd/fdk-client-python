"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .SendOtpEmailCommsTemplate import SendOtpEmailCommsTemplate

from .SendOtpEmailCommsProvider import SendOtpEmailCommsProvider


class SendOtpCommsReqEmail(BaseSchema):
    # Communication swagger.json

    
    otp_length = fields.Int(required=False)
    
    expiry = fields.Int(required=False)
    
    template = fields.Nested(SendOtpEmailCommsTemplate, required=False)
    
    provider = fields.Nested(SendOtpEmailCommsProvider, required=False)
    

