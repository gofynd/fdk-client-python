"""Rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Offer import Offer





from .ShareMessages import ShareMessages



from .ReferralDetailsUser import ReferralDetailsUser



class ReferralDetailsResponse(BaseSchema):
    #  swagger.json

    
    referral = fields.Nested(Offer, required=False)
    
    referrer_info = fields.Str(required=False)
    
    share = fields.Nested(ShareMessages, required=False)
    
    user = fields.Nested(ReferralDetailsUser, required=False)
    
