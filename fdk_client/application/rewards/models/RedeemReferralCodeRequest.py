"""rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class RedeemReferralCodeRequest(BaseSchema):
    #  swagger.json

    
    device_id = fields.Str(required=False)
    
    referral_code = fields.Str(required=False)
    
