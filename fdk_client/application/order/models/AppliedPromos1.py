"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .AppliedFreeArticles1 import AppliedFreeArticles1











class AppliedPromos1(BaseSchema):
    #  swagger.json

    
    amount = fields.Float(required=False)
    
    promotion_type = fields.Str(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles1, required=False), required=False)
    
    promo_id = fields.Str(required=False)
    
    article_quantity = fields.Float(required=False)
    
    promotion_name = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
