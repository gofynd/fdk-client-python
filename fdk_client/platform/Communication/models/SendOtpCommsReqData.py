"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class SendOtpCommsReqData(BaseSchema):
    #  swagger.json

    
    send_same_otp_to_channel = fields.Boolean(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    to = fields.Str(required=False)
    
