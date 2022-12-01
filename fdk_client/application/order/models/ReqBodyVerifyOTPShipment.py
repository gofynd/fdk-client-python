"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ReqBodyVerifyOTPShipment(BaseSchema):
    #  swagger.json

    
    request_id = fields.Str(required=False)
    
    otp_code = fields.Str(required=False)
    
