"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .DisplayBreakup import DisplayBreakup



from .CouponBreakup import CouponBreakup



from .RawBreakup import RawBreakup



from .LoyaltyPoints import LoyaltyPoints



class CartBreakup(BaseSchema):
    #  swagger.json

    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    