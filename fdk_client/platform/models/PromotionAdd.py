"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DisplayMeta1 import DisplayMeta1

from .DiscountRule import DiscountRule









from .PromotionAuthor import PromotionAuthor









from .Restrictions1 import Restrictions1







from .PromotionDateMeta import PromotionDateMeta

from .Visibility import Visibility

from .PromotionAction import PromotionAction

from .Ownership1 import Ownership1

from .PromotionSchedule import PromotionSchedule






class PromotionAdd(BaseSchema):
    # Cart swagger.json

    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    apply_priority = fields.Int(required=False)
    
    calculate_on = fields.Str(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    promo_group = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    stackable = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    currency = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    

