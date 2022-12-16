"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DisplayMeta1 import DisplayMeta1





from .Restrictions1 import Restrictions1



from .PromotionAuthor import PromotionAuthor











from .Visibility import Visibility



from .PromotionDateMeta import PromotionDateMeta





from .PromotionSchedule import PromotionSchedule



from .DiscountRule import DiscountRule



from .PromotionAction import PromotionAction















from .Ownership1 import Ownership1



class PromotionUpdate(BaseSchema):
    #  swagger.json

    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    code = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    buy_rules = fields.Dict(required=False)
    
    apply_priority = fields.Int(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    stackable = fields.Boolean(required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    
    promo_group = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
