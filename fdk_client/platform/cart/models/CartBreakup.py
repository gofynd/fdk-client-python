"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CouponBreakup import CouponBreakup



from .LoyaltyPoints import LoyaltyPoints



from .DisplayBreakup import DisplayBreakup



from .RawBreakup import RawBreakup



class CartBreakup(BaseSchema):
    #  swagger.json

    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
