"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ItemCriteria import ItemCriteria



from .DiscountOffer import DiscountOffer







class DiscountRule(BaseSchema):
    #  swagger.json

    
    item_criteria = fields.Nested(ItemCriteria, required=False)
    
    offer = fields.Nested(DiscountOffer, required=False)
    
    discount_type = fields.Str(required=False)
    
    buy_condition = fields.Str(required=False)
    
