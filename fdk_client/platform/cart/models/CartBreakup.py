"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .RawBreakup import RawBreakup



from .CouponBreakup import CouponBreakup



from .DisplayBreakup import DisplayBreakup



from .LoyaltyPoints import LoyaltyPoints



class CartBreakup(BaseSchema):
    #  swagger.json

    
    raw = fields.Nested(RawBreakup, required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
