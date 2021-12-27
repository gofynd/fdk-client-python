"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CouponBreakup import CouponBreakup

from .DisplayBreakup import DisplayBreakup

from .RawBreakup import RawBreakup

from .LoyaltyPoints import LoyaltyPoints


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    

