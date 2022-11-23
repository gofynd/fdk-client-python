"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .SendOtpSmsCommsTemplate import SendOtpSmsCommsTemplate



from .SendOtpSmsCommsProvider import SendOtpSmsCommsProvider



class SendOtpCommsReqSms(BaseSchema):
    #  swagger.json

    
    otp_length = fields.Int(required=False)
    
    expiry = fields.Int(required=False)
    
    template = fields.Nested(SendOtpSmsCommsTemplate, required=False)
    
    provider = fields.Nested(SendOtpSmsCommsProvider, required=False)
    
