"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class AddBeneficiaryViaOtpVerificationRequest(BaseSchema):
    #  swagger.json

    
    request_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    
    hash_key = fields.Str(required=False)
    
