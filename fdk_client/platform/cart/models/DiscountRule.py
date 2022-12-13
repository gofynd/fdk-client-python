"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .DiscountOffer import DiscountOffer



from .ItemCriteria import ItemCriteria





class DiscountRule(BaseSchema):
    #  swagger.json

    
    buy_condition = fields.Str(required=False)
    
    offer = fields.Nested(DiscountOffer, required=False)
    
    item_criteria = fields.Nested(ItemCriteria, required=False)
    
    discount_type = fields.Str(required=False)
    
