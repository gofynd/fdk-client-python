"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UsesRestriction1 import UsesRestriction1





from .UserRegistered import UserRegistered





from .PromotionPaymentModes import PromotionPaymentModes









from .PostOrder1 import PostOrder1



class Restrictions1(BaseSchema):
    #  swagger.json

    
    uses = fields.Nested(UsesRestriction1, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    user_registered = fields.Nested(UserRegistered, required=False)
    
    order_quantity = fields.Int(required=False)
    
    payments = fields.List(fields.Nested(PromotionPaymentModes, required=False), required=False)
    
    anonymous_users = fields.Boolean(required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    post_order = fields.Nested(PostOrder1, required=False)
    