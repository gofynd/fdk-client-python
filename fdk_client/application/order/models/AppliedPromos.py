"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .AppliedFreeArticles import AppliedFreeArticles















class AppliedPromos(BaseSchema):
    #  swagger.json

    
    applied_free_articles = fields.Nested(AppliedFreeArticles, required=False)
    
    promotion_type = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    promotion_name = fields.Str(required=False)
    
    article_quantity = fields.Float(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    promo_id = fields.Str(required=False)
    
