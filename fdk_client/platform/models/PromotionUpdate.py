"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Ownership1 import Ownership1



from .PromotionAuthor import PromotionAuthor

from .Restrictions1 import Restrictions1





from .DiscountRule import DiscountRule





from .PromotionSchedule import PromotionSchedule

from .Visibility import Visibility



from .PromotionDateMeta import PromotionDateMeta











from .DisplayMeta1 import DisplayMeta1

from .PromotionAction import PromotionAction




class PromotionUpdate(BaseSchema):
    # Cart swagger.json

    
    ownership = fields.Nested(Ownership1, required=False)
    
    application_id = fields.Str(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    stackable = fields.Boolean(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    mode = fields.Str(required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    promo_group = fields.Str(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    promotion_type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    
    apply_priority = fields.Int(required=False)
    

