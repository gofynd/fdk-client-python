"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SendOtpCommsReqData import SendOtpCommsReqData



from .SendOtpCommsReqSms import SendOtpCommsReqSms



from .SendOtpCommsReqEmail import SendOtpCommsReqEmail



class SendOtpCommsReq(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(SendOtpCommsReqData, required=False)
    
    sms = fields.Nested(SendOtpCommsReqSms, required=False)
    
    email = fields.Nested(SendOtpCommsReqEmail, required=False)
    
