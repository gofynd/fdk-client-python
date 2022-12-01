"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class VerifyOtpCommsReq(BaseSchema):
    #  swagger.json

    
    request_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    
