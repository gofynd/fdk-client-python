"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DisplayBreakup import DisplayBreakup



from .LoyaltyPoints import LoyaltyPoints



from .RawBreakup import RawBreakup



from .CouponBreakup import CouponBreakup



class CartBreakup(BaseSchema):
    #  swagger.json

    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
