"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .UsesRestriction import UsesRestriction

from .PostOrder import PostOrder





from .PriceRange import PriceRange

from .BulkBundleRestriction import BulkBundleRestriction


class Restrictions(BaseSchema):
    # Cart swagger.json

    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    payments = fields.Dict(required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
