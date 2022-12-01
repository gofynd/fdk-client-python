"""rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class ReferralDetailsUser(BaseSchema):
    #  swagger.json

    
    blocked = fields.Boolean(required=False)
    
    points = fields.Float(required=False)
    
    redeemed = fields.Boolean(required=False)
    
    referral_code = fields.Str(required=False)
    
