"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class AppliedPromotion(BaseSchema):
    #  swagger.json

    
    mrp_promotion = fields.Boolean(required=False)
    
    promo_id = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    promotion_type = fields.Str(required=False)
    
    article_quantity = fields.Int(required=False)
    
