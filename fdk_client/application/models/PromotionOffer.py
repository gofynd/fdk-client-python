"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .FreeGiftItems import FreeGiftItems














class PromotionOffer(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    free_gift_items = fields.List(fields.Nested(FreeGiftItems, required=False), required=False)
    
    valid_till = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    promotion_group = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Dict(required=False), required=False)
    
    description = fields.Str(required=False)
    

