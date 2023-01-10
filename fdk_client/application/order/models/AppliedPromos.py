"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .AppliedFreeArticles import AppliedFreeArticles











class AppliedPromos(BaseSchema):
    #  swagger.json

    
    promo_id = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    promotion_type = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    article_quantity = fields.Float(required=False)
    
    promotion_name = fields.Str(required=False)
    
