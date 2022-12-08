"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .BulkBundleRestriction import BulkBundleRestriction



from .UsesRestriction import UsesRestriction



from .PostOrder import PostOrder



from .PriceRange import PriceRange



class Restrictions(BaseSchema):
    #  swagger.json

    
    payments = fields.Dict(required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
