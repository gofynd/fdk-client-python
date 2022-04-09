"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    amount = fields.Float(required=False)
    
    promo_id = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    article_quantity = fields.Int(required=False)
    

