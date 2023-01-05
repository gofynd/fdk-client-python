"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LoyaltyPoints import LoyaltyPoints



from .CouponBreakup import CouponBreakup



from .DisplayBreakup import DisplayBreakup



from .RawBreakup import RawBreakup



class CartBreakup(BaseSchema):
    #  swagger.json

    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
