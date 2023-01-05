"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PromotionPaymentModes import PromotionPaymentModes





from .UsesRestriction1 import UsesRestriction1





from .UserRegistered import UserRegistered



from .PostOrder1 import PostOrder1









class Restrictions1(BaseSchema):
    #  swagger.json

    
    payments = fields.List(fields.Nested(PromotionPaymentModes, required=False), required=False)
    
    anonymous_users = fields.Boolean(required=False)
    
    uses = fields.Nested(UsesRestriction1, required=False)
    
    order_quantity = fields.Int(required=False)
    
    user_registered = fields.Nested(UserRegistered, required=False)
    
    post_order = fields.Nested(PostOrder1, required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
