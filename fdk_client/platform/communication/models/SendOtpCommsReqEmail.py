"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .SendOtpEmailCommsTemplate import SendOtpEmailCommsTemplate



class SendOtpCommsReqEmail(BaseSchema):
    #  swagger.json

    
    otp_length = fields.Int(required=False)
    
    expiry = fields.Int(required=False)
    
    template = fields.Nested(SendOtpEmailCommsTemplate, required=False)
    
