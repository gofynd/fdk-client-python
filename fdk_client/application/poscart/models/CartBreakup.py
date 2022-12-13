"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .LoyaltyPoints import LoyaltyPoints



from .RawBreakup import RawBreakup



from .CouponBreakup import CouponBreakup



from .DisplayBreakup import DisplayBreakup



class CartBreakup(BaseSchema):
    #  swagger.json

    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
