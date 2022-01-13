"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .DiscountOffer import DiscountOffer

from .ItemCriteria import ItemCriteria


class DiscountRule(BaseSchema):
    # Cart swagger.json

    
    discount_type = fields.Str(required=False)
    
    buy_condition = fields.Str(required=False)
    
    offer = fields.Nested(DiscountOffer, required=False)
    
    item_criteria = fields.Nested(ItemCriteria, required=False)
    
