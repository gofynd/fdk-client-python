"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class VerifyOtp(BaseSchema):
    #  swagger.json

    
    otp_code = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
