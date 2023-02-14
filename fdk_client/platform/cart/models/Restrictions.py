"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PostOrder import PostOrder







from .UsesRestriction import UsesRestriction



from .BulkBundleRestriction import BulkBundleRestriction









from .PriceRange import PriceRange





class Restrictions(BaseSchema):
    #  swagger.json

    
    post_order = fields.Nested(PostOrder, required=False)
    
    payments = fields.Dict(required=False)
    
    user_type = fields.Str(required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
