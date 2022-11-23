"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class VerifyOtp(BaseSchema):
    #  swagger.json

    
    request_id = fields.Str(required=False)
    
    otp_code = fields.Int(required=False)
    
