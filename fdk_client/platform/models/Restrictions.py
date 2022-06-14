"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .BulkBundleRestriction import BulkBundleRestriction

from .UsesRestriction import UsesRestriction



from .PriceRange import PriceRange



from .PostOrder import PostOrder


class Restrictions(BaseSchema):
    # Cart swagger.json

    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    payments = fields.Dict(required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    

