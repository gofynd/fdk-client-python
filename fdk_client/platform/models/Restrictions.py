"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .UsesRestriction import UsesRestriction

from .BulkBundleRestriction import BulkBundleRestriction



from .PriceRange import PriceRange





from .PostOrder import PostOrder




class Restrictions(BaseSchema):
    # Cart swagger.json

    
    payments = fields.Dict(required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    

