"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DiscountOffer import DiscountOffer







from .ItemCriteria import ItemCriteria



class DiscountRule(BaseSchema):
    #  swagger.json

    
    offer = fields.Nested(DiscountOffer, required=False)
    
    discount_type = fields.Str(required=False)
    
    buy_condition = fields.Str(required=False)
    
    item_criteria = fields.Nested(ItemCriteria, required=False)
    
