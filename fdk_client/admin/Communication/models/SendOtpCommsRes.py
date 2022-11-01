"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SendOtpCommsResSms import SendOtpCommsResSms



from .SendOtpCommsResEmail import SendOtpCommsResEmail



class SendOtpCommsRes(BaseSchema):
    #  swagger.json

    
    sms = fields.Nested(SendOtpCommsResSms, required=False)
    
    email = fields.Nested(SendOtpCommsResEmail, required=False)
    
