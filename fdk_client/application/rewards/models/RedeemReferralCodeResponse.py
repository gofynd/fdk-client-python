"""rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class RedeemReferralCodeResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    points = fields.Float(required=False)
    
    redeemed = fields.Boolean(required=False)
    
    referrer_id = fields.Str(required=False)
    
    referrer_info = fields.Str(required=False)
    
