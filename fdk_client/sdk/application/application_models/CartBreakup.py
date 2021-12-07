"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .RawBreakup import RawBreakup

from .LoyaltyPoints import LoyaltyPoints

from .DisplayBreakup import DisplayBreakup

from .CouponBreakup import CouponBreakup


class CartBreakup(BaseSchema):

    
    raw = fields.Nested(RawBreakup, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    

