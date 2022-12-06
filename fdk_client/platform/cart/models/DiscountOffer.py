"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class DiscountOffer(BaseSchema):
    #  swagger.json

    
    max_offer_quantity = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    min_offer_quantity = fields.Int(required=False)
    
    discount_price = fields.Float(required=False)
    
    discount_percentage = fields.Float(required=False)
    
    discount_amount = fields.Float(required=False)
    
    max_discount_amount = fields.Float(required=False)
    
