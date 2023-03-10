"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BulkBundleRestriction import BulkBundleRestriction

from .PostOrder import PostOrder

from .UsesRestriction import UsesRestriction







from .PriceRange import PriceRange




class Restrictions(BaseSchema):
    # Cart swagger.json

    
    payments = fields.Dict(required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    

