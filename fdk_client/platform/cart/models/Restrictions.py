"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .BulkBundleRestriction import BulkBundleRestriction



from .PriceRange import PriceRange











from .PostOrder import PostOrder



from .UsesRestriction import UsesRestriction





class Restrictions(BaseSchema):
    #  swagger.json

    
    coupon_allowed = fields.Boolean(required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
    payments = fields.Dict(required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    user_type = fields.Str(required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
